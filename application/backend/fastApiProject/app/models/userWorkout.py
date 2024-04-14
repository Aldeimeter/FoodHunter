# models.userWorkout.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class UserWorkout(Base):
    __tablename__ = "userWorkout"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    exercises_id = Column(Integer, ForeignKey("exercises.id"))
