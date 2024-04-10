# db/init_db.py
from .session import engine
from .base_class import Base
from models.user import User

def init_db() -> None:
    # create tables
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
