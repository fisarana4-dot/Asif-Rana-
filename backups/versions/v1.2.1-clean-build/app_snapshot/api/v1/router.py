from fastapi import APIRouter

from app.api.v1.endpoints import decision
from app.api.v1.endpoints import xai

router = APIRouter()

router.include_router(decision.router)
