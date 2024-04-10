# schemas/user.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# User Base schema to include common attributes
class UserBase(BaseModel):
    email: EmailStr

    class Config:
        from_attributes = True 
# Schema for user creation
class UserCreate(UserBase):
    password: str
    class Config:
        from_attributes = True 

# Schema for updating user information
class UserUpdate(UserBase):
    email: Optional[EmailStr] = None

    class Config:
        from_attributes = True 

# Schema for response model that hides certain information like hashed_password
class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    # Config to tell Pydantic to work with ORM objects
    class Config:
        from_attributes = True 

class UserOut(UserBase):
    email:str
    # Config to tell Pydantic to work with ORM objects
    class Config:
        from_attributes = True 
