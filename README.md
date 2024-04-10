# Filestructure
## Api 
package with endpoints stuff
* dependencies.py - all dependencies for endpoint, e.g. get_current_user (token authorization check)
### routers 
package for routers, each entity has it's own router

## Core
Some important functions, e.g., password hashing, Bearer token decode/encode

## Crud
CRUD for entities

## db
 some db config stuff
 * base_class -> Use "from db.base_class import Base" in your models
 * init_db - db tables creation and seeding, don't forget to import your model before running, run through 
"cd app"
"python -m db.init_db"
 * session -> session maker, infact get_db is used as dependency in routes

## models 
sqlalchemy models

## schemas 
pydantic schemas


