from sql import models as _models
import sql.database as _database

# create database
def create_database():
    """
    Creates the database based on the basemodel in _models.
    """
    return _database.Base.metadata.create_all(bind=_database.engine)

# create dependency
def get_db():
    """
    Creates database session and attempts to access database.
    Always closes the database when finished.
    """
    # create session
    db = _database.SessionLocal()
    try:
        yield db
    finally: # no matter what, close db
        db.close()