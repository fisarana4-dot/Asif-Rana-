from fastapi import FastAPI
from app.api.v1.router import router
from app.api import auth

app = FastAPI(title="NEXRA V16000")
app.add_api_route("/health", lambda: {"status":"ok","system":"NEXRA V16000"}, methods=["GET"])

app.include_router(router)
app.include_router(auth.router)
