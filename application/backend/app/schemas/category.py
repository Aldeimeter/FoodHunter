# schemas/category.py

from pydantic import BaseModel
from typing import List

class SubcategorySchema(BaseModel):
    subcategory: str
    subcategory_slug: str

class CategorySchema(BaseModel):
    category: str
    category_slug: str
    subcategories: List[SubcategorySchema]

    class Config:
        from_attributes = True
