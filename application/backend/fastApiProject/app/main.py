from fastapi import FastAPI
from api.routers.auth import router as auth  
from api.routers.category import router as category  
from api.routers.food import router as food
from api.routers.meal import router as meal
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, String


app = FastAPI()
app.include_router(auth, tags=["Auth"], prefix="/auth")
app.include_router(category, tags=["Category"]) 
app.include_router(food, tags=["Food"], prefix="/food")
app.include_router(meal, tags=["Meal"], prefix="/meal")

if __name__ == "__main__":
    import os
    import uvicorn
    if not os.path.exists('images'):
        os.makedirs('images')
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
