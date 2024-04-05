from sqlalchemy import Column, Integer, String, ForeignKey, Table
from app.core.config import settings
import sqlalchemy.orm as orm
from typing import List
from app.models.component_model import ComponentModel


product_components = Table(
    'product_components',
    settings.DBBaseModel.metadata,
    Column('id_component', Integer, ForeignKey('components.id')),
    Column('id_product', Integer, ForeignKey('products.id'))
)


class ProductModel(settings.DBBaseModel):
    __tablename__ = "products" 
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image = Column(String, nullable=True, default="")
    category_id = Column(Integer, ForeignKey("categories.id"))
    group_id = Column(Integer, ForeignKey("groups.id"))
    
    category = orm.relationship("CategoryModel", lazy="joined") 
    group = orm.relationship("GroupModel", lazy="joined")
    components: List[ComponentModel] = orm.relationship(
        'ComponentModel', 
        secondary=product_components, 
        backref='comp', 
        lazy='joined'
    )
    
    @property
    def get_components_list(self):
        list_components: List[int] = []

        for component in self.components:
            list_components.append(int(component.id))
        
        return list_components
    