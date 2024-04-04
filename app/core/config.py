import os
from pydantic.v1 import BaseConfig
from dotenv import load_dotenv
from fastapi.templating import Jinja2Templates
from pathlib import Path
from sqlalchemy.ext.declarative import declarative_base

load_dotenv(".env")


class Settings(BaseConfig):
    DB_URL: str = os.getenv("DB_URL")
    DBBaseModel = declarative_base()
    TEMPLATES = Jinja2Templates(directory="templates")
    MEDIA = Path("media")
    AUTH_COOKIE_NAME: str = os.getenv("AUTH_COOKIE_NAME")
    SALTY: str = os.getenv("SALTY")
    
    class Config:
        case_sensitive = True


settings: Settings = Settings()
