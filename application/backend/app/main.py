from fastapi import FastAPI
from api.routers.auth import router as auth  
from api.routers.category import router as category  
from api.routers.food import router as food
from api.routers.meal import router as meal
import os

app = FastAPI()
app.include_router(auth, tags=["Auth"], prefix="/auth")
app.include_router(category, tags=["Category"]) 
app.include_router(food, tags=["Food"], prefix="/food")
app.include_router(meal, tags=["Meal"], prefix="/meal")

@app.get("/check_health")
async def check_server():
    return {"message": "Server is reachable"}

if __name__ == "__main__":
    if not os.path.exists('images'):
        os.makedirs('images')
    uvicorn.run("main:app", host=os.getenv("HOST_IP"), port=8000, reload=True)
