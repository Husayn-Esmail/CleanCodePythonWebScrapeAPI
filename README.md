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
a file to store data because files get messy. I recommend deleting the current 
database file so that none of the existing entries conflict with what is being
tested.

The due date for this project is May 11, 2022. 

LIMITATIONS:
The limitations of this project is that it cannot reach into iframes. Nor can it
deal with authentication and complexities like that.

### [ATTENTION]:
This API can somewhat handle javascript heavy pages as well as infinite scroll
pages but it has not been tested entirely. If you would like to use this feature,
uncomment the specified line in search.py. By default it will not handle such
tasks because I thought it was outside the scope of this project and things get
quite a bit more complex and slower when selenium is introduced.

To start the virtual environment:
source pyapi/bin/activate

To leave the virtual environment: 
deactivate

Once you've entered the virtual environment, you can start the API with start.sh. 
NOTE: If running outside the virtual environment, this will only work if you've 
installed the required dependencies, but since the virtual environment has been 
uploaded as well, the dependencies should come with it. 


Check requirements.txt for the necessary libraries to run this API. <br>
To install packages from requirements.txt run the following command:
pip3 install -r requirements.txt


Explanation of files:
- sql holds all database related files (except the database and main interface)
- database.py holds the code which runs the database
- main.py houses all the main functionality including the app and endpoints
- models.py holds python representations of the table in the database
- schemas.py holds the code that validates type before information is entered to database
- crud.py holds read and write functions for the database
- services.py is the gateway between main.py and the database
- tagselect.db is the database
- templates is a folder holding the html for the api endpoints
- form.html the code for the api interface 
- static holds css files
- stylesheet.css has styles for form.html
- search.py holds functions for searching the given webpage
