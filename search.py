import fastapi as _fastapi
import requests as _requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from chromedriver_py import binary_path

def get_html_string(link):
    """
    Uses Selenium to simulate a browser and return the complete html string
    from a website. Note that the functionality has only been tested briefly and
    that the result will contain utf-8 characters. This function will not be
    actively used unless you decide to uncomment the alternative html_string
    variable below. If you go this route, ensure to comment the other html_string.
    Returns a string of the html code.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    s = Service(binary_path)
    driver = webdriver.Chrome(service=s,options=chrome_options)
    try:
        driver.get(link)
    except:
        raise _fastapi.HTTPException(status_code=400, detail="The url you entered is not valid")
    page = driver.page_source.encode("utf-8")
    # page = page.decode("utf-8")
    # page = page.encode("ascii","ignore")
    page = str(page) # done separately to make it easier when testing
    driver.quit()
    return page

def find_element(link, string):
    """
    Takes a link (string), and a string (string) as parameters. The link is
    the url used to search the string against. A get request is performed on the
    link which is converted to lowercase text. Then rfind is performed to find
    the last occurrance of the desired string. A loop works both backwards and
    forwards until the whole element is found. 
    Returns the element (string).
    """
    try:
        html_string = _requests.get(link).text
    except: 
        raise _fastapi.HTTPException(status_code=400, detail="The url you entered is not valid")
    # html_string = get_html_string(link) # uncomment this line to handle js heavy pages
    # find last occurrence of string (returns index of first character)
    result_index = html_string.lower().rfind(string)
    # starting/ending character indexes
    start_index = result_index
    end_index = result_index
    # starting/ending character
    start = html_string[start_index]
    end = html_string[end_index]

    # get full element
    while (start != "<"): # find index of the opening tag
        start_index -= 1
        start = html_string[start_index]

    while (end != ">"): # find index of closing tag
        end_index += 1
        end = html_string[end_index]

    # return the element
    return html_string[start_index:end_index+1]

def get_result(link, string):
    """
    Takes a link (string) and string (string) as paramaters and finds the
    element containing that string. This is a separate function because it
    also includes some error checking, namely the case where the desired string
    does not appear on the webpage.
    Returns a result of the whole process (string).
    """
    # find the element
    result = find_element(link, string)
    # checking if the element could be found
    result = "not found" if result == "" else result
    return result

