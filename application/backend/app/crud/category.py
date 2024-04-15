# crud/category.py

from sqlalchemy.orm import Session
from models.category import Category
from typing import List, Dict
from collections import defaultdict

def get_categories_with_subcategories(db: Session) -> List[Dict]:
    results = db.query(
        Category.category,
        Category.category_slug,
        Category.subcategory,
        Category.subcategory_slug
    ).all()

    category_dict = defaultdict(list)
    for cat, cat_slug, subcat, subcat_slug in results:
        category_dict[(cat, cat_slug)].append({'subcategory': subcat, 'subcategory_slug': subcat_slug})

    return [
        {"category": cat, "category_slug": cat_slug, "subcategories": subs}
        for (cat, cat_slug), subs in category_dict.items()
    ]
