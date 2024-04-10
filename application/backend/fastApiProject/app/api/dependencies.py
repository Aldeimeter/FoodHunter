# app/api/dependencies.py 

from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from db.session import get_db
from fastapi import HTTPException, status, Depends
import jwt
from core import security
from crud import user as crud_user
import schemas.user as schemas

def get_current_user(db:Session = Depends(get_db), token: str = Depends(security.oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate":"Bearer"},
    )

    payload = security.decode_access_token(token)
    username: str = payload.get("sub")
    if not username:
        raise credentials_exception
    
    user = crud_user.get_user_by_email(db, email=username)
    if user is None:
        raise credentials_exception
    
    return schemas.UserOut.from_orm(user)
