import requests as _requests

def find_element(link, string):
    """
    Takes a link (string), and a string (string) as parameters. The link is
    the url used to search the string against. A get request is performed on the
    link which is converted to lowercase text. Then rfind is performed to find
    the last occurrance of the desired string. A loop works both backwards and
    forwards until the whole element is found. 
    Returns the element (string).
    """
    html_string = _requests.get(link).text
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

