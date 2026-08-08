from pydantic import BaseModel, HttpUrl
from typing import Optional


class CompanyProfile(BaseModel):
    company_name: str
    industry: Optional[str] = None
    country: Optional[str] = None
    website: Optional[HttpUrl] = None
    employee_range: Optional[str] = None
    technology_signals: list[str] = []
