from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.decision_repo import DecisionRepository
from app.schemas.decisions import DecisionCreate, TradingSignalSchema
from app.services.trading_signal_service import TradingSignalService
from app.services.risk_manager_service import RiskManagerService
from app.core.logging import logger
import json

class DecisionService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repo = DecisionRepository(db)
        self.signal_service = TradingSignalService()
        self.risk_service = RiskManagerService()

    async def process_decision(self, data: DecisionCreate):
        logger.info(f"Processing decision {data.decision_id} through Service Layer...")
        
        # 1. Identify asset based on payload
        asset = "GOLD" if "gold" in data.input_payload.lower() else "BTC"
        
        # 2. Generate Trading Signal
        signal = await self.signal_service.generate_signal(asset=asset, data={"input": data.input_payload})
        
        # 3. Evaluate Risk
        risk_result = await self.risk_service.evaluate_risk(signal)
        
        # 4. Determine final status based on risk approval
        final_status = "completed" if risk_result["is_approved"] else "rejected"
        output_data = {
            "signal": signal.dict(),
            "risk_evaluation": risk_result
        }
        
        # 5. Save Decision to DB
        new_decision = await self.repo.create_decision(
            decision_id=data.decision_id,
            input_payload=data.input_payload,
            output_result=json.dumps(output_data),
            status=final_status
        )
        return new_decision
