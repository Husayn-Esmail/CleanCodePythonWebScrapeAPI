
import fastapi as _fastapi
import fastapi.responses as _responses
import fastapi.staticfiles as _static
import fastapi.templating as _template
import sqlalchemy.orm as _orm
import sql.schemas as schemas
import sql.crud as crud
import search, services

# init fastapi
app = _fastapi.FastAPI()
# where to find static files
app.mount("/static", _static.StaticFiles(directory="static"), name="static")
# where to find templates
templates = _template.Jinja2Templates(directory="templates")
# create database
services.create_database()

# endpoint to serve the form (interface)
@app.get("/form", response_class=_responses.HTMLResponse)
def form_post(request: _fastapi.Request):
    """
    Handles get requests to the endpoint so user can submit a post request.
    """
    # return the form
    return templates.TemplateResponse("form.html", context={"request": request})


# endpoint to accept input from the form
@app.post("/form", response_model=schemas.Query)
def form_post(
    request: _fastapi.Request,
    query: schemas.Query = _fastapi.Depends(schemas.Query.as_form),
    db: _orm.Session = _fastapi.Depends(services.get_db)
    ):
    """
    Handles form post requests and gets the desired results from database
    or scrapes web for new queries.
    Returns the form template with the new found result.
    """
    # set user input to lowercase to maintain case insensitive
    query.link = query.link.lower()
    query.qstring = query.qstring.lower()

    services.work_with_db(db=db, query=query)
    # main functionality, read docstring in services.py for more information
    # returns user back to the form with new found element only, nothing else.
    return templates.TemplateResponse("form.html", context={'request': request, "result": query.element})


@app.post("/api", response_model=schemas.Query)
def get_element( 
    query: schemas.Query,
    db: _orm.Session = _fastapi.Depends(services.get_db)
    ):
    # set input to lowercase to maintain case insensitive
    query.link = query.link.lower()
    query.qstring = query.qstring.lower()
    # main functionality, read docstring in services.py for more information
    services.work_with_db(db=db, query=query)
    # return input and output
    # return {
    #     "url": query.link, 
    #     "search string": query.qstring,
    #     "html element": query.element
    # }
    return query

@app.get("/api/{link:path}", response_model=schemas.Query)
def show_element(
    query: schemas.Query = _fastapi.Depends(),
    db: _orm.Session = _fastapi.Depends(services.get_db)
):
    query.link = query.link.lower()
    query.qstring = query.qstring.lower()
    services.work_with_db(db=db, query=query)
    return query