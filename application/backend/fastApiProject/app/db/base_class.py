# db/base_class.py
from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    id = None  # Overridden by subclasses
    __name__: str  # Avoids Pydantic complaints

    # Generate __tablename__ automatically from the model class name.
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() +'s'
