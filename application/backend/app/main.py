from fastapi import FastAPI
from app.api.routers.auth import router as auth
from app.db import session
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, String

app = FastAPI()
app.include_router(auth, tags=["Auth"], prefix="/auth")


