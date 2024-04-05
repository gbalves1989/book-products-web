from sqlalchemy import Column, Integer, String
from app.core.config import settings


class UserModel(settings.DBBaseModel):
    __tablename__ = "users" 
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    avatar = Column(String, nullable=True, default="")
    