# api.routers/category.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from crud.category import get_categories_with_subcategories
from schemas.user import UserOut
from schemas.category import CategorySchema
from db.session import get_db
import api.dependencies as dependencies

router = APIRouter()

@router.get("/categories", response_model=List[CategorySchema])
def read_categories(db: Session = Depends(get_db), current_user: UserOut = Depends(dependencies.get_current_user)):
    categories = get_categories_with_subcategories(db)
    return categories
