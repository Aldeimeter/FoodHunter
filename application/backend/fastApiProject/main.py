from fastapi import FastAPI
##from router import router
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, String

app = FastAPI()
##app.include_router(router)

app_database = "postgresql://tvorca:hahaha@localhost:5432/application"
engine = create_engine(app_database)
app_metadata = MetaData()

users = Table('users', app_metadata,
              Column('id', Integer, primary_key=True, autoincrement=True, nullable=False),
              Column('username', String, nullable=False),
              Column('email', String, nullable=False)
              )

exercises = Table('exercises', app_metadata,
                  Column('id', Integer, primary_key=True, autoincrement=True, nullable=False),
                  Column('name', String, nullable=False),
                  Column('description', String, nullable=False))

food = Table('food', app_metadata,
             Column('id', Integer, primary_key=True, autoincrement=True, nullable=False),
             Column('name', String, nullable=False),
             Column('proteins', String, nullable=False),
             Column('fats', String, nullable=False),
             Column('carbohydrates', String, nullable=False),
             Column('calories', String, nullable=False))

app_metadata.create_all(engine)

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
