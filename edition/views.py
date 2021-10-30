from django.shortcuts import render

from book.models import Book
from .models import Edition

def edition(request, slug):
    edition = Edition.objects.get(slug=slug)
    books = Book.objects.filter(edition__slug=slug)
    context = {
        'edition': edition,
        'books': books
    }
    return render(request, 'edition.html', context)

def listOfEditions(request):
    editions = Edition.objects.all().order_by('title')
    context = {
        'editions': editions
    }
    
    return render(request, 'listOfEditions.html', context)
