from sqlalchemy import Column, Integer, String
from app.core.config import settings


class CategoryModel(settings.DBBaseModel):
    __tablename__ = "categories" 
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String, nullable=False, unique=True)
    