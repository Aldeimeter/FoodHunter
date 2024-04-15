# models/category.py
from sqlalchemy import Column, Integer, String, TIMESTAMP, Index
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship 
from db.base_class import Base
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, nullable=False)
    subcategory = Column(String, nullable=False)
    
    category_slug = Column(String, nullable=False)
    subcategory_slug = Column(String, nullable=False)

    food = relationship("Food", back_populates="category") 
    # set timestamp on creation
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    # set timestamp on update
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())
    
    __table_args__ = (
        Index('ix_category_subcategory', 'category', 'subcategory', unique=True),
    )
