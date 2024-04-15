# seed_categories.py 

from sqlalchemy.orm import Session
from db.base_class import Base 
from db.session import engine 
from models.user import User
from models.category import Category
from models.food import Food
from sqlalchemy.exc import IntegrityError


categories_data = [
    {"category": "Fruits and Vegetables", "subcategory": "Fresh Fruits", "category_slug": "fruits-and-vegetables", "subcategory_slug": "fresh-fruits"},
    {"category": "Fruits and Vegetables", "subcategory": "Fresh Vegetables", "category_slug": "fruits-and-vegetables", "subcategory_slug": "fresh-vegetables"},
    {"category": "Fruits and Vegetables", "subcategory": "Legumes and Beans", "category_slug": "fruits-and-vegetables", "subcategory_slug": "legumes-and-beans"},
    {"category": "Fruits and Vegetables", "subcategory": "Nuts and Seeds", "category_slug": "fruits-and-vegetables", "subcategory_slug": "nuts-and-seeds"},

    {"category": "Dairy and Egg Products", "subcategory": "Milk and Cream", "category_slug": "dairy-and-egg-products", "subcategory_slug": "milk-and-cream"},
    {"category": "Dairy and Egg Products", "subcategory": "Cheese", "category_slug": "dairy-and-egg-products", "subcategory_slug": "cheese"},
    {"category": "Dairy and Egg Products", "subcategory": "Yogurt", "category_slug": "dairy-and-egg-products", "subcategory_slug": "yogurt"},
    {"category": "Dairy and Egg Products", "subcategory": "Eggs", "category_slug": "dairy-and-egg-products", "subcategory_slug": "eggs"},

    {"category": "Meat and Poultry", "subcategory": "Beef", "category_slug": "meat-and-poultry", "subcategory_slug": "beef"},
    {"category": "Meat and Poultry", "subcategory": "Pork", "category_slug": "meat-and-poultry", "subcategory_slug": "pork"},
    {"category": "Meat and Poultry", "subcategory": "Chicken", "category_slug": "meat-and-poultry", "subcategory_slug": "chicken"},
    {"category": "Meat and Poultry", "subcategory": "Turkey", "category_slug": "meat-and-poultry", "subcategory_slug": "turkey"},
    {"category": "Meat and Poultry", "subcategory": "Lamb", "category_slug": "meat-and-poultry", "subcategory_slug": "lamb"},

    {"category": "Seafood", "subcategory": "Fish", "category_slug": "seafood", "subcategory_slug": "fish"},
    {"category": "Seafood", "subcategory": "Shellfish", "category_slug": "seafood", "subcategory_slug": "shellfish"},
    {"category": "Seafood", "subcategory": "Crustaceans", "category_slug": "seafood", "subcategory_slug": "crustaceans"},

    {"category": "Grains and Cereals", "subcategory": "Bread and Pastries", "category_slug": "grains-and-cereals", "subcategory_slug": "bread-and-pastries"},
    {"category": "Grains and Cereals", "subcategory": "Rice", "category_slug": "grains-and-cereals", "subcategory_slug": "rice"},
    {"category": "Grains and Cereals", "subcategory": "Pasta", "category_slug": "grains-and-cereals", "subcategory_slug": "pasta"},
    {"category": "Grains and Cereals", "subcategory": "Cereals", "category_slug": "grains-and-cereals", "subcategory_slug": "cereals"},

    {"category": "Sweets and Snacks", "subcategory": "Chocolate and Candy", "category_slug": "sweets-and-snacks", "subcategory_slug": "chocolate-and-candy"},
    {"category": "Sweets and Snacks", "subcategory": "Snack Foods", "category_slug": "sweets-and-snacks", "subcategory_slug": "snack-foods"},
    {"category": "Sweets and Snacks", "subcategory": "Ice Cream and Desserts", "category_slug": "sweets-and-snacks", "subcategory_slug": "ice-cream-and-desserts"},

    {"category": "Beverages", "subcategory": "Coffee and Tea", "category_slug": "beverages", "subcategory_slug": "coffee-and-tea"},
    {"category": "Beverages", "subcategory": "Soft Drinks", "category_slug": "beverages", "subcategory_slug": "soft-drinks"},
    {"category": "Beverages", "subcategory": "Juices", "category_slug": "beverages", "subcategory_slug": "juices"},
    {"category": "Beverages", "subcategory": "Alcoholic Beverages", "category_slug": "beverages", "subcategory_slug": "alcoholic-beverages"},

    {"category": "Condiments and Sauces", "subcategory": "Spices and Herbs", "category_slug": "condiments-and-sauces", "subcategory_slug": "spices-and-herbs"},
    {"category": "Condiments and Sauces", "subcategory": "Sauces and Dressings", "category_slug": "condiments-and-sauces", "subcategory_slug": "sauces-and-dressings"},
    {"category": "Condiments and Sauces", "subcategory": "Cooking Oils and Fats", "category_slug": "condiments-and-sauces", "subcategory_slug": "cooking-oils-and-fats"},

    {"category": "Prepared and Processed Foods", "subcategory": "Frozen Meals", "category_slug": "prepared-and-processed-foods", "subcategory_slug": "frozen-meals"},
    {"category": "Prepared and Processed Foods", "subcategory": "Canned Goods", "category_slug": "prepared-and-processed-foods", "subcategory_slug": "canned-goods"},
    {"category": "Prepared and Processed Foods", "subcategory": "Instant and Ready-to-Eat Meals", "category_slug": "prepared-and-processed-foods", "subcategory_slug": "instant-and-ready-to-eat-meals"},

    {"category": "Specialty Foods", "subcategory": "Organic Products", "category_slug": "specialty-foods", "subcategory_slug": "organic-products"},
    {"category": "Specialty Foods", "subcategory": "Gluten-Free Products", "category_slug": "specialty-foods", "subcategory_slug": "gluten-free-products"},
    {"category": "Specialty Foods", "subcategory": "Vegan and Vegetarian Foods", "category_slug": "specialty-foods", "subcategory_slug": "vegan-and-vegetarian-foods"},
    {"category": "Specialty Foods", "subcategory": "Ethnic and International Foods", "category_slug": "specialty-foods", "subcategory_slug": "ethnic-and-international-foods"},
]

def seed_categories(db: Session, categories_data: list):
    for cat_data in categories_data:
        category = Category(
            category=cat_data["category"],
            subcategory=cat_data["subcategory"],
            category_slug=cat_data["category_slug"],
            subcategory_slug=cat_data["subcategory_slug"]                   
        )
        db.add(category)
    try:
        db.commit()
        print("Categories have been seeded successfully.")
    except IntegrityError:
        print("Categories already exist. No new categories were added.")
        db.rollback()
    finally:
        db.close()

def wrapped_seeder():
    session = Session(bind=engine)
    seed_categories(session, categories_data)
