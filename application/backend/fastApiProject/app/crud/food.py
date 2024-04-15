# crud/food.py

from sqlalchemy.orm import Session
from sqlalchemy import or_
from models.food import Food
from schemas.food import FoodCreate, FoodUpdate, FoodRead
from models.category import Category
from typing import List

# Create a new food entry
def create(db: Session, food_create: FoodCreate) -> Food:
    food = Food(**food_create.dict())
    db.add(food)
    db.commit()
    db.refresh(food)
    return food

# Get a list of food entries
def get_list(db: Session, skip: int = 0, limit: int = 100) -> List[Food]:
    return db.query(Food).offset(skip).limit(limit).all()

# Search through food list 
def search(db: Session, query: str, skip: int = 0, limit: int = 100) -> List[Food]:
    return db.query(Food).filter(
            or_(
                Food.name.ilike(f'%{query}%'),  # Case-insensitive 'like' for name
                Food.description.ilike(f'%{query}%')  # Case-insensitive 'like' for description
            )
        ).offset(skip).limit(limit).all()

# Get food list by category slug
def get_food_list_by_category_slug(db: Session, category_slug: str, skip: int = 0, limit: int = 100) -> List[Food]:
    return (
        db.query(Food)
        .join(Category, Category.id == Food.category_id)
        .filter(Category.category_slug == category_slug)
        .offset(skip)
        .limit(limit)
        .all()
    )

# Get food list by category and subcategory slug
def get_list_by_category_subcategory_slug(db: Session, category_slug: str, subcategory_slug: str, skip: int = 0, limit: int = 100) -> List[Food]:
    return (
        db.query(Food)
        .join(Category, Category.id == Food.category_id)
        .filter(Category.category_slug == category_slug, Category.subcategory_slug == subcategory_slug)
        .offset(skip)
        .limit(limit)
        .all()
    )

# Get a single food entry by ID
def get_by_id(db: Session, food_id: int) -> FoodRead:
    return db.query(Food).filter(Food.id == food_id).first()

# Get a single food entry by barcode
def get_by_barcode(db: Session, barcode: str) -> Food:
    return db.query(Food).filter(Food.barcode == barcode).first()

# Update food entry
def update(db: Session, food_id: int, food_update: FoodUpdate) -> Food:
    food = db.query(Food).filter(Food.id == food_id).first()
    if food:
        update_data = food_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(food, key, value)
        db.commit()
        db.refresh(food)
    return food

# Delete food entry
def delete(db: Session, food_id: int) -> None:
    food = db.query(Food).filter(Food.id == food_id).first()
    if food:
        db.delete(food)
        db.commit()
