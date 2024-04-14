from sqlalchemy import Column, Integer, String
# from app.db.base_class import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    description = Column(String, index=True)

    def __init__(self, name, category, description):
        self.name = name
        self.category = category
        self.description = description
