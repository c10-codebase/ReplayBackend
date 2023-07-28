from pydantic import BaseSettings, Field
import os

class Settings(BaseSettings):
    class Config:
        env_file = os.environ.get("ENV_FILE") or '.env'
        env_file_encoding = 'utf-8'
        
    PROJECT_NAME: str = "Replay_Backend"
    OPEN_API_URL: str = "/api/v1/openapi.json"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "A7+rJXccZYy1TZqJsN46mXlHXxGGAmzJWh52Y69AeZU="
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    db_user:str ="postgres"
    db_pass:str ="adhi1998"
    db_host:str ="127.0.0.1"
    db_port:int = 5432
    database:str ="replayback"
    
settings = Settings() 