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
    # query the database for all existing entries that match the specified link
    db_entries = crud.get_queries_by_link(db=db, link=query.link)

    # If no entries were found that match the link
    if (db_entries == []):
        # complete the query structure with the element
        query.element = search.get_result(query.link, query.qstring)
        # add query to the database
        print("called")
        crud.create_query(db=db, query=query)
    else: # this only needs to be performed if db_entries is not empty
        count = 0
        # db_entries is not empty and there could be multiple entries
        for entry in db_entries:
            # all entries in db_entries will match link, just check for qstring
            if (entry.qstring.lower() == query.qstring):
                print("read")
                query.element = entry.element
                break
            count += 1
        # If the whole list was traversed without a match, add query to database
        if (count == len(db_entries)):
            query.element = search.get_result(query.link, query.qstring)
            print("called2")
            crud.create_query(db=db, query=query)
    # returns user back to the form with new found element only, nothing else.
    return templates.TemplateResponse("form.html", context={'request': request, "result": query.element})
