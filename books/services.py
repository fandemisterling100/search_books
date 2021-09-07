"""Service layer to make the request to the corresponding
EndPoint at  https://openlibrary.org/developers/api."""


import requests
from requests.models import Response

URL = "http://openlibrary.org/search.json"
SEARCH_LIMIT = 10

def create_books_dictionary(response):
    
    docs = response.get("docs")[:SEARCH_LIMIT]
    #import pdb; pdb.set_trace()
    books = []
    
    for result in docs:
        
        author = result.get("author_name")
        author = author[0] if author else "No Author"
        subject = result.get("subject")
        subject = ", ".join(subject) if subject else "No Subject"
        isbn = result.get("isbn")
        isbn = isbn[0] if isbn else "No ISBN"
        
        books.append(
            {
                "title": result.get("title"),
                "author": author,
                "isbn": isbn,
                "publish_date": result.get("first_publish_year"),
                "publisher": "Publisher",
                "subject": subject
            }
        )
        
    return books

def response_handler(response):
    
    if response.status_code == 200:

        return create_books_dictionary(response.json())
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