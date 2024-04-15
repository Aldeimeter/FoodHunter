# api.routers/food.py

from decimal import Decimal
from fastapi import APIRouter, Depends, HTTPException, Query, Path, File, Form, UploadFile, Response
from dataclasses import dataclass
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from schemas.user import UserOut
from db.session import get_db
import api.dependencies as dependencies
from typing import List, Optional
import crud.food as crud 
from schemas.food import FoodCreate, FoodRead, FoodUpdate
from core import images
router = APIRouter()

@router.post("/", response_model=FoodRead)
async def create_food_item(food_in: FoodCreate = Depends(dependencies.parse_food_create), 
                           image: UploadFile = File(None),
                           db: Session = Depends(get_db), 
                           current_user: UserOut = Depends(dependencies.get_current_user)):
    if image:
        image_id = await images.save_image(image)
        food_in.image_id = image_id 
    food = crud.create(db=db, food_create=food_in)
    return food


@router.get("/", response_model=List[FoodRead])
async def read_food_items(category_slug: str = Query(None, description="The slug of category"), 
                    subcategory_slug: str = Query(None, descripiton="The slug of subcategory"),
                    skip: int = 0, limit: int = 100, 
                    db: Session = Depends(get_db), 
                    current_user: UserOut = Depends(dependencies.get_current_user)):
    if category_slug is None:
        return crud.get_list(db, skip=skip, limit=limit)
    if subcategory_slug is None:
        return crud.get_food_list_by_category_slug(db,
                                                   category_slug=category_slug, 
                                                   skip=skip,
                                                   limit=limit)
    return crud.get_list_by_category_subcategory_slug(db,
                                                      category_slug=category_slug, 
                                                      subcategory_slug=subcategory_slug, 
                                                      skip=skip,
                                                      limit=limit)


@router.get("/search",response_model=List[FoodRead])
async def search(query: str = Query(..., description="The search query"), 
                 skip: int = 0,
                 limit: int = 100, 
                 db: Session = Depends(get_db), 
                 current_user: UserOut = Depends(dependencies.get_current_user)):
    food = crud.search(db, query=query, skip=skip, limit=limit)
    if not food:
        raise HTTPException(status_code=404, detail="No matching food found")
    return food 

@router.get("/{food_identifier}", response_model=FoodRead)
async def read_food_item(food_identifier: str = Path(..., 
                                                     title="Food Identifier", 
                                                     description="An ID or a barcode of the food"),
                         db: Session = Depends(get_db), 
                         current_user: UserOut = Depends(dependencies.get_current_user)):
    if food_identifier.isdigit() and len(food_identifier) <= 5:
        food = crud.get_by_id(db,food_id=int(food_identifier))
    elif food_identifier.isdigit() and len(food_identifier) > 5:
        food = crud.get_by_barcode(db, barcode=food_identifier)
    else:
        raise HTTPException(status_code=400, detail="Invalid identifier format")

    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    return food


@router.put("/{food_id}", response_model=FoodRead)
async def update_food_item(food_id: int,
                           food_in: FoodUpdate,
                           db: Session = Depends(get_db),
                           current_user: UserOut = Depends(dependencies.get_current_user)):
    food = crud.get_by_id(db, food_id=food_id)
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    food = crud.update(db=db, food_id=food_id, food_update=food_in)
    return food


@router.delete("/{food_id}", status_code=200)
async def delete_food_item(food_id: int,
                           db: Session = Depends(get_db),
                           current_user: UserOut = Depends(dependencies.get_current_user)):
    food = crud.get_by_id(db, food_id=food_id)
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    crud.delete(db=db, food_id=food_id)
    return {"message": "Food deleted successfully"}

@router.get("/images/{food_id}")
async def get_food_image(food_id: int, 
                         db: Session = Depends(get_db),
                         current_user: UserOut = Depends(dependencies.get_current_user)):
    food = crud.get_by_id(db, food_id=food_id)
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    
    path = images.get_image_path(food.image_id)
    if not path:
        raise HTTPException(status_code=404, detail="Image not found")

    return FileResponse(path)
