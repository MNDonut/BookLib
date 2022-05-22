from django.shortcuts import render

from book.models import Book
from .models import Edition

def edition(request, slug):
    edition = Edition.objects.get(slug=slug)
    books = Book.objects.filter(edition__slug=slug).order_by('title')
    context = {
        'edition': edition,
        'books': books
    }
    return render(request, 'edition.html', context)

def listOfEditions(request):
    editions = Edition.objects.all().order_by('title')
    listOfLetters = []
    for edition in editions:
        letter = str(edition.title)[0].upper() 
        if letter.upper() not in listOfLetters:
            listOfLetters.append(letter.upper())

    letterAndEdition = {}
    for letter in listOfLetters:
        letterAndEdition[letter] = \
            [edition for edition in editions if str(edition.title).upper().startswith(letter)]
            
    context = {
        'letterAndEdition': letterAndEdition
    }
    
    return render(request, 'listOfEditions.html', context)
