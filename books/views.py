from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    
    return render(request, "books/index.html", {
        "message": None
    })

def search(request):
    
    title = request.POST["title"]
    author = request.POST["author"]
    print(title)
    print(author)
    if (title is None or title == "") and (author is None or author == ""):
        return render(request, "books/index.html", {
        "message": "You should enter an author or title value to start your search"
    })
    
    return HttpResponse("Funciona! {} {}".format(title, author))
