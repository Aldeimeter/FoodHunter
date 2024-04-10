from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from db.base_class import Base
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    # set timestamp on creation
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    # set timestamp on update
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())
    
