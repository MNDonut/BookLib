from django.shortcuts import render

from book.models import Book
from .models import Author

def author(request, slug):
    author = Author.objects.get(slug=slug)
    books = Book.objects.filter(author__slug=slug)
    context = {
        'author': author,
        'books': books
    }
    return render(request, 'author.html', context)

def listOfAuthors(request):
    authors = Author.objects.all().order_by('firstname')
    context = {
        'authors': authors
    }
    
    return render(request, 'listOfAuthors.html', context)
