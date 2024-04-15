# crud/meal.py
from sqlalchemy.orm import Session
from sqlalchemy import Date
from datetime import date
from models.meal import Meal
from schemas.meal import MealCreate, MealUpdate
from typing import List, Optional

# Create a new meal entry
def create(db: Session, meal_create: MealCreate) -> Meal:
    meal = Meal(**meal_create.dict())
    db.add(meal)
    db.commit()
    db.refresh(meal)
    return meal

# Get a list of meal entries by day
def get_list_by_day(db: Session, meal_date: date, user_id: int, skip: int = 0, limit: int = 100) -> List[Meal]:
    return (
        db.query(Meal)
        .filter(Meal.created_at.cast(Date) == meal_date, Meal.user_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )

# Get a single meal entry by ID
def get_by_id(db: Session, meal_id: int) -> Optional[Meal]:
    return db.query(Meal).filter(Meal.id == meal_id).first()

# Update meal entry
def update(db: Session, meal_id: int, meal_update: MealUpdate) -> Optional[Meal]:
    meal = db.query(Meal).filter(Meal.id == meal_id).first()
    if meal:
        update_data = meal_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(meal, key, value)
        db.commit()
        db.refresh(meal)
        return meal
    return None

# Delete meal entry
def delete(db: Session, meal_id: int) -> None:
    meal = db.query(Meal).filter(Meal.id == meal_id).first()
    if meal:
        db.delete(meal)
        db.commit()
