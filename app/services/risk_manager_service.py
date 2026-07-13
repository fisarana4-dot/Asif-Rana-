from app.core.logging import logger
from app.schemas.decisions import TradingSignalSchema

class RiskManagerService:
    def __init__(self):
        self.max_risk_limit = 0.7  # 70% max risk limit

    async def evaluate_risk(self, signal: TradingSignalSchema) -> dict:
        logger.info(f"Evaluating risk for signal: {signal.action} {signal.asset}")
        
        # Simulated risk calculation (if confidence is high, risk is lower)
        calculated_risk = 0.4 if signal.confidence > 0.8 else 0.8
        is_approved = calculated_risk <= self.max_risk_limit
        
        # Update signal with calculated risk score
        signal.risk_score = calculated_risk
        
        return {
            "is_approved": is_approved,
            "risk_score": calculated_risk,
            "reason": "Risk is within acceptable limits." if is_approved else "Risk too high! Action blocked."
        }
