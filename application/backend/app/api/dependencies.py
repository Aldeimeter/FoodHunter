# app/api/dependencies.py 

import json
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from db.session import get_db
from fastapi import HTTPException,Security, status, Depends, Form
import jwt
from core import security
from crud import user as crud_user
import schemas.user as schemas_user
import schemas.food as schemas_food

def get_current_user(db: Session = Depends(get_db), token: str = Security(security.oauth2_scheme) ) -> schemas_user.UserOut:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = security.decode_access_token(token)

        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception

    user = crud_user.get_user_by_email(db, email=username)
    if user is None:
        raise credentials_exception

    return schemas_user.UserOut.from_orm(user)


async def parse_food_create(food_in: str = Form(...)) -> schemas_food.FoodCreate:
    try:
        # Attempt to load the JSON data from the form field
        food_data = json.loads(food_in)
        # Validate the data using the Pydantic model
        food_create = schemas_food.FoodCreate(**food_data)
        return food_create
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON format: {str(e)}")
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=f"Validation error: {e.errors()}")
