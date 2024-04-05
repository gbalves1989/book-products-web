from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.config import settings
import sqlalchemy.orm as orm


class ComponentModel(settings.DBBaseModel):
    __tablename__ = "components" 
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    
    product = orm.relationship("ProductModel", lazy="joined")
    