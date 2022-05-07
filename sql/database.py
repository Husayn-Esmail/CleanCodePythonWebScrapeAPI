import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

# all of this code was obtained from fastapi tutorial documentation and
# restructured to suit my needs.

# Database location
SQLALCHEMY_DATABASE_URL = "sqlite:///./queries.db"

# create database engine
engine = _sql.create_engine (
    # setup for sqlite
    SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False}
)

# used to create database sessions
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base for models to inherit from
Base = _declarative.declarative_base()
