This API is supposed to return the HTML element that contains a given text
string on a given web page. The API has an endpoint that takes the URL and
text search string as arguments and stores them in a database.
If a query already exists in the database, then it should return the stored
value rather than re-scraping the website. If the web page has more than one
matching element, then the last element should be returned from the API.

I have decided to use fastapi because I think it will be faster than django
This API is written in python and has been written by Husayn Esmail. I also 
decided to use sqlite because while it would be better to use postgres for
production, I did not intend to use it for production. In any case, switching
to postgres should be relatively easy if that is desired. I opted against using
a file to store data because files get messy.

The due date for this project is May 11, 2022. 

LIMITATIONS:
The limitations of this project is that it cannot handle infinite scrolling
websites, and it cannot reach into iframes. As of May 6, 2022 it also can't
deal with javascript intensive websites, but I'm working on that and hopefully
it will be completed by the due date.

To start the virtual environment:
source pyapi/bin/activate

To leave the virtual environment: 
deactivate

Once you've entered the virtual environment, you can start the API with start.sh. 
NOTE: If running outside the virtual environment, this will only work if you've 
installed the required dependencies, but since the virtual environment has been 
uploaded as well, the dependencies should come with it. 


Check requirements.txt for the necessary libraries to run this API.
To install packages from requirements.txt run the following command
pip3 install -r requirements.txt

A few other things to note:
ignore scrape.py, I wanted to track it's history but it was really just for testing
the scraping functionality in isolation. Also ignore crud.py, it is not being used
and was a part of a previous attempt.

Explanation of other files:
database.py holds the code which runs the database
main.py houses all the main functionality including the app and endpoints
models.py holds python representations of the table in the database
schemas.py holds the code that validates type before information is entered to database
services.py is the gateway between main.py and the database
tagselect.db is the database
templates is a folder holding the html for the api endpoints
form.html the code for the api interface 
landing.html is the code for the root path
static holds css files
stylesheet.css has styles for form.html
