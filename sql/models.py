import sqlalchemy as _sql
from . import database

# most of this code was obtained from fastapi tutorial documentation and
# restructured to suit my needs.

# python representation of database table
class Query(database.Base):
    """
    Inherits from the Base class setup in database.py.
    This class represents a Query for the html element surrounding a given
    string on a given webpage.
    Specifies the table in the database.
    link is a string that should store the url of a given webpage
    qstring is a string that should store the given search string
    element is a string that should store the element containing the given
    search string, or 'not found' if the element could not be found.
    """
    # name of table
    __tablename__ = "queries"
    # columns in table, id is necessary for primary key but is never used.
    id = _sql.Column(_sql.Integer, primary_key=True, index=True, unique=True)
    link = _sql.Column(_sql.String, index=True)
    qstring = _sql.Column(_sql.String, index=True)
    # set default value to empty
    element = _sql.Column(_sql.String, index=True, default="")
