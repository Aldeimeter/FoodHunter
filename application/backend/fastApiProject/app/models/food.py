from sqlalchemy import Column, Integer, String
# from app.db.base_class import Base
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Food(Base):
    __tablename__ = "food"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    proteins = Column(Integer, index=True)
    carbohydrates = Column(Integer, index=True)
    fats = Column(Integer, index=True)

    def __init__(self, name, proteins, carbohydrates, fats):
        self.name = name
        self.proteins = proteins
        self.carbohydrates = carbohydrates
        self.fats = fats
