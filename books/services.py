"""Service layer to make the request to the corresponding
EndPoint at  https://openlibrary.org/developers/api."""


import requests
from requests.models import Response

URL = "http://openlibrary.org/search.json"

def response_handler(response):
    
    if response.status_code == 200:
        return response.json()
    else:
        return 0

def get_books(url, params):
    
    response = requests.get(url, params=params)
    return response_handler(response)


def get_books_handler(title, author):
    
    no_title = title is None or title == ""
    no_author = author is None or author == ""
    
    if no_title:
        params = {"author": author}
        
    elif no_author: 
        params = {"title": title}
        
    else:
        params = {"author": author, "title": title}
        
    books = get_books(URL, params)
     
    return books