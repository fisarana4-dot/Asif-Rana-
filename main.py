from fastapi import FastAPI
from app.database.session import engine, Base
from app.core.config import settings
from app.api.v1.endpoints import decisions

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Enterprise AI Decision Operating System (Phase 2)",
    version="2.0.0"
)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def root():
    return {
        "status": "online",
        "system": settings.PROJECT_NAME,
        "stage": "Phase 2 - Enterprise Architecture Ready"
    }

app.include_router(decisions.router, prefix=settings.API_V1_STR + "/decisions", tags=["Decisions"])
