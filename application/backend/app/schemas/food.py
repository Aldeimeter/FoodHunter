# schemas/food.py

from typing import Optional
from pydantic import BaseModel, validator
from decimal import Decimal

class FoodSchema(BaseModel):
    name: str
    description: str
    calories: Decimal
    carbohydrates: Decimal
    sugars: Decimal
    proteins: Decimal
    fats: Decimal
    saturated_fats: Decimal
    fibers: Decimal
    is_custom: bool
    barcode: Optional[str] = None
    category_id: int
    image_id: Optional[str] = None

    @validator('*', pre=True)
    def convert_decimal(cls, v):
        if isinstance(v, float):
            return Decimal(str(v))
        return v

    class Config:
        from_attributes = True
        json_encoders = {
            Decimal: lambda v: f"{v:.2f}"
        }
# Schema for food creation
class FoodCreate(FoodSchema):
    author_id: int

# Schema for reading food data
class FoodRead(FoodSchema):
    id: int
    image_id: Optional[str] = None
    
    class Config:
        from_attributes = True

# Schema for updating food data
class FoodUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    calories: Optional[float] = None
    carbohydrates: Optional[float] = None
    sugars: Optional[float] = None
    proteins: Optional[float] = None
    fats: Optional[float] = None
    saturated_fats: Optional[float] = None
    fibers: Optional[float] = None
    image_id: Optional[str] = None

# Schema for food deletion
class FoodDelete(BaseModel):
    id: int
