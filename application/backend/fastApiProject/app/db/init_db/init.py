# db.init_db/init.py
from db.session import engine
from db.init_db.seed_categories import wrapped_seeder as cat_seed 
from db.base_class import Base
from models.user import User
from models.category import Category
from models.food import Food
def init_db() -> None:
    # drop tables
    Base.metadata.drop_all(bind=engine)
    print("Tables dropped")
    # create tables
    Base.metadata.create_all(bind=engine)
    print("Tables created")
    # seed tables 
    cat_seed()

if __name__ == "__main__":
    init_db()
