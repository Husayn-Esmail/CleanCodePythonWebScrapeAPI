import sqlalchemy.orm as _orm
from . import models, schemas

# most of this code was obtained from fastapi tutorial documentation and
# restructured to suit my needs.

# get all queries that match the link provided
def get_queries_by_link(db: _orm.Session, link: str):
    """
    Takes a database (_orm.Session) and a link (string) as input and 
    returns a list of Query objects from the database that match the link. 
    """
    return db.query(models.Query).filter(models.Query.link == link).all()

def create_query(db: _orm.Session, query: schemas.Query):
    """
    Takes a database (_orm.Session) and a query (schemas.Query) then creates,
    adds and commits that quer to the database.
    Returns the Query object.
    """
    db_query = models.Query(link=query.link, qstring=query.qstring, element=query.element)
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query

