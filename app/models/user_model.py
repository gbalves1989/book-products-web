from sqlalchemy import Column, Integer, String
from app.core.config import settings


class UserModel(settings.DBBaseModel):
    __tablename__ = "users" 
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String, nullable=False)
    email: str = Column(String, nullable=False, unique=True)
    password: str = Column(String, nullable=False)
    avatar: str = Column(String, nullable=True, default="")
    