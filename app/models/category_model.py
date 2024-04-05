from sqlalchemy import Column, Integer, String
from app.core.config import settings


class CategoryModel(settings.DBBaseModel):
    __tablename__ = "categories" 
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    