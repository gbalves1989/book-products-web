from sqlalchemy import Column, Integer, String
from app.core.config import settings


class ProductModel(settings.DBBaseModel):
    __tablename__ = "products" 
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    code: str = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image = Column(String, nullable=True, default="")