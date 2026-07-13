from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database.models import DecisionHistory

class DecisionRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_decision(self, decision_id: str, input_payload: str, output_result: str, status: str) -> DecisionHistory:
        db_decision = DecisionHistory(
            decision_id=decision_id,
            input_payload=input_payload,
            output_result=output_result,
            status=status
        )
        self.db.add(db_decision)
        await self.db.flush()
        return db_decision

    async def get_by_decision_id(self, decision_id: str) -> DecisionHistory | None:
        result = await self.db.execute(
            select(DecisionHistory).where(DecisionHistory.decision_id == decision_id)
        )
        return result.scalars().first()

    async def get_all_decisions(self, limit: int = 100):
        result = await self.db.execute(select(DecisionHistory).limit(limit))
        return result.scalars().all()
