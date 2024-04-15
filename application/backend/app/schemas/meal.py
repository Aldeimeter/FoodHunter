# schemas/meal.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MealBase(BaseModel):
    mass: float
    meal_type: str
    user_id: int
    food_id: int

class MealCreate(MealBase):
    pass

class MealRead(MealBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True

class MealUpdate(BaseModel):
    mass: Optional[float] = None
    meal_type: Optional[str] = None

