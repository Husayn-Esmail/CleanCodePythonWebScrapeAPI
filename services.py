import sqlalchemy.orm as _orm
# all my modules are imported without protection
from sql import database, schemas, crud
import search
# create database
def create_database():
    """
    Creates the database based on the Base variable in database.
    Obtained from fastapi tutorial documentaion.
    """
    return database.Base.metadata.create_all(bind=database.engine)

# create dependency
def get_db():
    """
    Creates database session and attempts to access database.
    Always closes the database when finished.
    Obtained from fastapi tutorial documentation
    """
    # create session
    db = database.SessionLocal()
    try:
        yield db
    finally: # no matter what, close db
        db.close()

def work_with_db(db: _orm.Session, query: schemas.Query):
    """
    This is in a separate file becuase I felt like this was a service that main
    was using. I had to reuse this code block and that made it necessary to turn
    it into a function. It expects query's input to be converted to lower
    first. I probably could have done that in here and maybe I will. I wasn't
    sure what to do so I left it out of this function.
    """
    # query the database for all existing entries that match the specified link
    db_entries = crud.get_queries_by_link(db=db, link=query.link)

    # If no entries were found that match the link
    if (db_entries == []):
        # complete the query structure with the element
        query.element = search.get_result(query.link, query.qstring)
        # add query to the database
        print("called") # proves scraping
        crud.create_query(db=db, query=query)
    else: # this only needs to be performed if db_entries is not empty
        count = 0
        # db_entries is not empty and there could be multiple entries
        for entry in db_entries:
            # all entries in db_entries will match link, just check for qstring
            if (entry.qstring.lower() == query.qstring):
                print("read") # proves reading from db instead of scraping again
                query.element = entry.element
                break
            count += 1
        # If the whole list was traversed without a match, add query to database
        if (count == len(db_entries)):
            query.element = search.get_result(query.link, query.qstring)
            print("called2") # proves scraping when qstring not in database is queried
            crud.create_query(db=db, query=query)
