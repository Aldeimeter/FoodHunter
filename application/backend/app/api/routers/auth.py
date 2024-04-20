from fastapi import APIRouter, Security, HTTPException, status, Depends
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
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud_user.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={
                "WWW-Authenticate" : "Bearer",
                "app-error" : "INVALID_CREDENTIALS",
            }
        )
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    ) 
    refresh_token_expires = timedelta(days=7) 
    refresh_token = security.create_refresh_token(
        data={"sub": user.email}
    )
    crud_user.set_refresh_token(db,user,refresh_token, refresh_token_expires)
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "refresh_token": refresh_token
    }


@router.post("/register", response_model=schemas.UserOut, summary="User Registration Endpoint")
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Email already registered. Please choose a different email.",
            headers = {"app-error": "EMAIL_IS_TAKEN"},
        )
    user = crud_user.create_user(db=db, user=user)
    return schemas.UserOut.from_orm(user)


@router.get("/me", response_model=schemas.UserOut, summary="Get Current User Endpoint")
def get_current_user(current_user: schemas.UserOut = Depends(dependencies.get_current_user)):
    return current_user


@router.post("/refresh", summary="Refresh Access Token")
def refresh_access_token(refresh_token: str, db: Session = Depends(get_db)):
    user = crud_user.get_user_by_refresh_token(db, refresh_token) 
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token")

    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)

    new_refresh_token_expires = timedelta(days=7)
    new_refresh_token = security.create_refresh_token(data={"sub": user.email}, expires_delta=new_refresh_token_expires)
    crud_user.set_refresh_token(db, user, new_refresh_token, new_refresh_token_expires)

    return {"access_token": access_token, "token_type": "bearer", "refresh_token": new_refresh_token}


@router.post("/logout", summary="Logout and Revoke Refresh Token")
async def logout_and_revoke_refresh_token(current_user: schemas.UserOut = Depends(dependencies.get_current_user), db: Session = Depends(get_db)):
    success = crud_user.invalidate_refresh_token(db, current_user.id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Token already invalidated"
        )
    return {"message": "Logged out successfully, refresh token revoked"}
