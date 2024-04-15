# api.router/meal

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from datetime import date
from models.meal import Meal
from schemas.meal import MealCreate, MealRead, MealUpdate
from schemas.user import UserOut
import crud.meal as crud
from db.session import get_db
import api.dependencies as dependencies

router = APIRouter()


@router.post("/", response_model=MealRead)
def create_meal(meal_data: MealCreate,
                db: Session = Depends(get_db),
                current_user: UserOut = Depends(dependencies.get_current_user)):
    return crud.create(db=db, meal_create=meal_data)


@router.get("/{meal_id}",response_model=MealRead)
def read_meal(meal_id: int,
              db: Session = Depends(get_db),
              current_user: UserOut = Depends(dependencies.get_current_user)):
    meal = crud.get_by_id(db=db, meal_id=meal_id)
    if meal is None:
        raise HTTPException(status_code=404, detail="Meal not found")
    return meal


@router.get("/by_date/", response_model=List[MealRead])
def read_meals_by_date(meal_date: date, 
                       user_id: int,
                       db: Session = Depends(get_db),
                       current_user: UserOut = Depends(dependencies.get_current_user)):
    return crud.get_list_by_day(db=db, meal_date=meal_date, user_id=user_id)


@router.put("/{meal_id}", response_model=MealRead)
def update_meal(meal_id: int,
                meal_update: MealUpdate, 
                db: Session = Depends(get_db),
                current_user: UserOut = Depends(dependencies.get_current_user)):
    updated_meal = crud.update(db=db, meal_id=meal_id, meal_update=meal_update)
    if updated_meal is None:
        raise HTTPException(status_code=404, detail="Meal not found")
    return updated_meal



@router.delete("/{meal_id}", status_code=204)
def delete_meal(meal_id: int, 
                db: Session = Depends(get_db),
                current_user: UserOut = Depends(dependencies.get_current_user)):
    existing_meal = crud.get_by_id(db=db, meal_id=meal_id)
    if not existing_meal:
        raise HTTPException(status_code=404, detail="Meal not found")
    crud.delete(db=db, meal_id=meal_id)
    return {"message": "Meal deleted successfully"}
