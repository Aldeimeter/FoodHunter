# models/user.py
from sqlalchemy import Column, Integer, String, TIMESTAMP, Text, DateTime
from datetime import datetime, timedelta
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship 
from db.base_class import Base
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    food = relationship("Food", back_populates="author")
    meals = relationship("Meal", back_populates="user")

    # refresh token stuff
    refresh_token = Column(Text, index=True, nullable=True)
    refresh_token_expires_at = Column(DateTime, nullable=True)

    # set timestamp on creation
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    # set timestamp on update
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())
