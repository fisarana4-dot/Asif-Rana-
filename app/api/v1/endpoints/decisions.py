from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.services.decision_service import DecisionService
from app.schemas.decisions import DecisionCreate, DecisionResponse

router = APIRouter()

@router.post("/", response_model=DecisionResponse, status_code=status.HTTP_201_CREATED)
async def create_decision_endpoint(payload: DecisionCreate, db: AsyncSession = Depends(get_db)):
    service = DecisionService(db)
    existing = await service.repo.get_by_decision_id(payload.decision_id)
    if existing:
        raise HTTPException(status_code=400, detail="Decision ID already exists")
    
    result = await service.process_decision(payload)
    return result
