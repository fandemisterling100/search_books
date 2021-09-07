"""Service layer to make the request to the corresponding
EndPoint at  https://openlibrary.org/developers/api
"""


import requests

# URL to make requests to the API
URL = "http://openlibrary.org/search.json"

# Maximum limit of books to show
SEARCH_LIMIT = 10


def create_books_dictionaries(response):
    """ Function to create a list of dictionaries
        with the information of title, author, ISBN,
        first year of publication, publisher and subject
        of each result.

        Inputs: response (json)
        Outputs: books (list)
    """

    # Select the subset of SEARCH_LIMIT books
    docs = response.get("docs")[:SEARCH_LIMIT]
    books = []

    # Iterate over the results to get basic info
    # from each book
    for result in docs:

        try:
            # Validations of fields for each result
            author = result.get("author_name")
            author = author[0] if author else "No Author"
            subject = result.get("subject")
            subject = ", ".join(subject) if subject else "No Subject"
            isbn = result.get("isbn")
            isbn = isbn[0] if isbn else "No ISBN"
            publisher = result.get("publisher")
            publisher = publisher[0] if publisher else "No publisher"

            # Build the dictionary with basic information
            books.append(
                {
                    "title": result.get("title"),
                    "author": author,
                    "isbn": isbn,
                    "publish_date": result.get("first_publish_year"),
                    "publisher": publisher,
                    "subject": subject
                }
            )
        except:
            books = None

    return books


def response_handler(response):
    """Function to know the status of the request
        to the API according to the parameters
        provided by the user

        Inputs: response (requests.models.Response)
        Outputs: 0 (int) if the result was not successful, a (list) otherwise
    """

    if response.status_code == 200:
        return create_books_dictionaries(response.json())
    else:
        return 0


def get_books(url, params):
    """ Function to make the request to the API

        Inputs: url (str), params (dict)
        Outputs: response (requests.models.Response)
    """

    response = requests.get(url, params=params)
    return response_handler(response)


def get_books_handler(title, author):
    """Function to build the parameter dictionary
        according to the values provided by the user
        to make the request.

        Inputs: title (str), author (str), or None if they
                were not provided.
        Outputs: 0 (int) if the result was not successful, a (list) otherwise
    """

    # Validation of existing parameters
    no_title = title is None or title == ""
    no_author = author is None or author == ""

    # Build the parameter dictionary
    if no_title:
        params = {"author": author}

    elif no_author:
        params = {"title": title}

    else:
        params = {"author": author, "title": title}

    # Get the books according to the parameters
    books = get_books(URL, params)

    return books
