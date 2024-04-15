# db/base_class.py
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id = None  # Overridden by subclasses
    __name__: str  # Avoids Pydantic complaints

