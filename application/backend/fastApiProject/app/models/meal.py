# models/meal.py 
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Boolean
from sqlalchemy.sql import func
from sqlalchemy.types import Numeric 
from sqlalchemy.orm import relationship 
from db.base_class import Base

class Meal(Base):
    __tablename__ = "meals"
    
    id = Column(Integer, primary_key=True, index=True)
    mass = Column(Numeric(10,2))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="meals")
    food_id= Column(Integer, ForeignKey("food.id"), nullable=False)
    food = relationship("Food", back_populates="meals")
    meal_type = Column(String, nullable=False)
     
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    # set timestamp on update
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())
