import os

class Config:
    APP_NAME = os.getenv("APP_NAME", "NEXRA_V16000")
    APP_ENV = os.getenv("APP_ENV", "development")
    DB_PATH = os.getenv("DB_PATH", "nexra_v16000.db")
xra_v16000.db")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
