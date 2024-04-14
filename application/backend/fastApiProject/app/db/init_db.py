# db/init_db.py
from session import engine, SessionLocal
# from .base_class import Base ##this won't work
from app.models.user import User
from app.models.exercises import Exercise
from app.models.food import Food


def init_db() -> None:
    # create tables
    Exercise.metadata.create_all(bind=engine)  # creating exercise table
    User.metadata.create_all(bind=engine)  # creating user table
    Food.metadata.create_all(bind=engine)

    # inserting initital data into tables
    session = SessionLocal()

    exercise1 = Exercise(name="Bench press", category="chest", description='Test Exercise 1')
    exercise2 = Exercise(name="Squat", category="legs", description='Test Exercise 2')
    exercise3 = Exercise(name="overhead press", category="shoulders", description='Test Exercise 3')
    exercise4 = Exercise(name="pull up", category="back", description='Test Exercise 4')
    exercise5 = Exercise(name="bicep curl", category="arms", description='Test Exercise 5')

    chicken = Food(name="chicken breast", proteins=32, carbohydrates=12, fats=2)
    rice = Food(name="rice", proteins=2, carbohydrates=58, fats=3)
    yogurt = Food(name="yogurt", proteins=4, carbohydrates=8, fats=14)
    kaiser = Food(name="kaiser", proteins=1, carbohydrates=21, fats=0)
    protein = Food(name="protein", proteins=24, carbohydrates=1, fats=0)

    session.add(exercise1)
    session.add(exercise2)
    session.add(exercise3)
    session.add(exercise4)
    session.add(exercise5)
    session.add(chicken)
    session.add(rice)
    session.add(yogurt)
    session.add(kaiser)
    session.add(protein)
    session.commit()
    session.close()


if __name__ == "__main__":
    init_db()
