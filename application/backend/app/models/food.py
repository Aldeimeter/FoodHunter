# models/food.py
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Boolean
from sqlalchemy.sql import func
from sqlalchemy.types import Numeric 
from sqlalchemy.orm import relationship 
from db.base_class import Base
class Food(Base):
    __tablename__ = "food"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    calories = Column(Numeric(10,2))
    carbohydrates = Column(Numeric(10,2))
    sugars = Column(Numeric(10,2))
    proteins = Column(Numeric(10,2))
    fats = Column(Numeric(10,2))
    saturated_fats = Column(Numeric(10,2))
    fibers = Column(Numeric(10,2))
    is_custom = Column(Boolean, default=False)
    barcode = Column(String, index=True, nullable=True)

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("Category", back_populates="food")
    
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    author = relationship("User", back_populates="food")
    meals = relationship("Meal", back_populates="food")
    image_id = Column(String, nullable=True)  # Assuming the image is not mandatory
    # set timestamp on creation
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    # set timestamp on update
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())
    
