import pydantic as _pydantic
import fastapi as _fastapi
import typing as _typing

# most of this code was obtained from fastapi tutorial documentation and
# restructured to suit my needs.
class QueryBase(_pydantic.BaseModel):
    """
    This is a base model for the Query class. All Query subclasses
    inherit from this class.
    Contains a link and a qstring only as the minimum information required.
    """
    link: str
    qstring: str

class QueryCreate(QueryBase):
    """
    Inherits from QueryBase, holds all columns.
    link, qstring and element as the database entry should only
    be created when all information is known to avoid having empty or missing
    information in any of the cells.
    That being said, element is an optional field because I wanted it to be
    consistent with the Query class. This class is used as a type.
    """
    link: str
    qstring: str
    element: _typing.Optional[str] = None

class Query(QueryBase):
    """
    Inherits from QueryBase, holds all columns. Since this class is being
    used for both reads and writes, element is optional because it's not
    populated at the time of data collection from the html form. Element is
    populated after actions have been performed on link and qstring. 
    There is a class method to make it compliant with html forms as they
    have different data output which is not equivalent to json. 
    HTML input names and attribute names in here must be consistent for the
    form to work. Note the class method code is not necessarily mine, it uses 
    my variable names but it's from a stack overflow post which I read but 
    didn't manage to get working without this video. He also mentions the stack
    overflow post.
    video link: https://www.youtube.com/watch?v=L4WBFRQB7Lk
    """
    link: str
    qstring: str
    element: _typing.Optional[str] = None

    # setup the object to be used as form input model
    @classmethod
    def as_form(
        cls,
        link: str = _fastapi.Form(...),
        qstring: str = _fastapi.Form(...),
        element: _typing.Optional[str] = None
    ):
        return cls(
            link = link,
            qstring = qstring,
            element = element
        )

