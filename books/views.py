from django.shortcuts import render
from django.http import HttpResponse
from .services import get_books_handler


def index(request):
    """Render the index page to start the search
    """

    return render(request, "books/index.html", {
        "message": None
    })


def search(request):
    """Search view to receive the values of author and title to
    call the API
    """

    # Get author and title
    title = request.POST.get("title")
    author = request.POST.get("author")

    # Server-side validation of the form to get at least one value
    if (title is None or title == "") and (author is None or author == ""):
        return render(request, "books/index.html", {
        "message": "You should enter an author or title value to start your search"
    })

    # Call API to get results
    books = get_books_handler(title, author)

    # Validate Response
    if books and books != 0:

        # Render results
        return render(request, 'books/results.html', {
            "books": books
        })
    elif books == 0:
        # Error in the request
        return render(request, 'books/results.html', {
            "books": None,
            "message": "We couldn't process your request, please try again."
        })
    elif not books:
        # Results not found
        return render(request, 'books/results.html', {
            "books": books,
            "message": "We couldn't find any matches"
        })
