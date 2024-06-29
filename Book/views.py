from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.
def booklist(request):
    books = models.Book.objects.all()
    context={'books':books}
    print(books)
    return render(request, 'Books/books.html',context)