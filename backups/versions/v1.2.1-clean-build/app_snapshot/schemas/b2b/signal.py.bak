from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class BusinessSignal(BaseModel):
    signal_type: str
    sour
ce: str
    evidence: str
    confidence_score: float = Field(ge=0, le=1)
    detected_at: Optional[datetime] = None
source: str
