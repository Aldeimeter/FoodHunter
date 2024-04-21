# crud/user.py
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from fastapi.encoders import jsonable_encoder
import models.user as models
import schemas.user as schemas
from datetime import timedelta, datetime 
from core.hashing import Hasher
from typing import List, Union
from sqlalchemy.orm import Session

def get_user(db: Session, user_id: int) -> models.User:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> models.User:
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user_by_refresh_token(db: Session, refresh_token: str):
    user = db.query(models.User).filter(
        models.User.refresh_token == refresh_token,
        models.User.refresh_token_expires_at > datetime.utcnow()
    ).first()
    if user:
        return user


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    db_user = models.User(email=user.email,
                          hashed_password=Hasher.get_password_hash(user.password),
                          refresh_token=None,
                          refresh_token_expires_at=None)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def set_refresh_token(db: Session, user: models.User, token: str, expires_delta: timedelta):
    user.refresh_token = token
    user.refresh_token_expires_at = datetime.utcnow() + expires_delta
    db.add(user)
    db.commit()


def invalidate_refresh_token(db: Session, user_id: int) -> bool:
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.refresh_token = None
        user.refresh_token_expires_at = None
        db.commit()
        return True
    return False
    

def delete_user(db: Session, user_id: int) -> bool:
    db_user = db.query(models.User).filter(models.User.id == user_id)
    if db_user.first():
        db_user.delete()
        db.commit()
        return True
    return False


def authenticate_user(db: Session, email: str, password: str) -> Union[bool, models.User]:
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not Hasher.verify_password(password, user.hashed_password):
        return False
    return user


