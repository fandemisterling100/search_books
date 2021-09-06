from django.shortcuts import render
from django.http import HttpResponse
from .services import get_books_handler

def index(request):
    """Render the index page to start the search"""
    
    return render(request, "books/index.html", {
        "message": None
    })

def search(request):
    """Search view to receive the values of author and title to 
    call the API"""
    
    # Get author and title
    title = request.POST["title"]
    author = request.POST["author"]

    # Server-side validation of the form to get at least one value
    if (title is None or title == "") and (author is None or author == ""):
        return render(request, "books/index.html", {
        "message": "You should enter an author or title value to start your search"
    })
    
    # Call API to get results
    books = [{
        "title": "Lord of the Rings",
        "author": "J. R. R. Tolkien",
        "publish_date": "October 2001",
        "publisher": "Coles Editorial Board",
        "isbn": "0774011181",
        "subject": "Motion pictures"
        }, {
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "publish_date": "1999 November 25",
        "publisher": "Scholastic Canada",
        "isbn": "9780747546290",
        "subject": "Fantasy fiction"
        }]
    books2 = get_books_handler(title, author)
    
    # Render results
    return render(request, 'books/results.html', {
        "books": books
    })
