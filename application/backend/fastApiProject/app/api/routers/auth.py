from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta 
from core import security
from crud import user as crud_user
from db.session import get_db
import schemas.user as schemas
from pydantic import ValidationError
import api.dependencies as dependencies
router = APIRouter()

@router.post("/login", summary="Token Authentication Endpoint")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud_user.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Incorrect username or password",
            headers = {"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register", response_model=schemas.UserOut, summary="User Registration Endpoint")
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Email already registered"
        )
    user = crud_user.create_user(db=db, user=user)
    return schemas.UserOut.from_orm(user)

@router.get("/me", response_model=schemas.UserOut, summary="Get Current User Endpoint")
def get_current_user(current_user: schemas.UserOut = Depends(dependencies.get_current_user)):
    return current_user
