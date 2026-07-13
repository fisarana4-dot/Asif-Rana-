from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class DecisionCreate(BaseModel):
    decision_id: str
    input_payload: str
    output_result: str
    status: str = "completed"

class DecisionResponse(BaseModel):
    id: int
    decision_id: str
    input_payload: str
    output_result: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

class TradingSignalSchema(BaseModel):
    asset: str = Field(..., description="The asset ticker, e.g., BTC, AAPL, GOLD")
    action: str = Field(..., description="BUY, SELL, or HOLD")
    price: float = Field(..., description="Target or current execution price")
    quantity: float = Field(..., description="Quantity to execute")
    confidence: float = Field(..., description="Confidence score between 0.0 and 1.0")
    risk_score: Optional[float] = None
