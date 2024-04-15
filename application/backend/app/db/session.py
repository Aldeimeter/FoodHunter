# db/session.py 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# db_url = "postgresql://postgres:GaX3jpTCAv-?ftKo@34.118.17.194:5432/application"
db_url = "postgresql://tvorca:hahaha@localhost:5432/application"


engine = create_engine(db_url, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally: 
        db.close()
