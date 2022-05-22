from django.shortcuts import render

from book.models import Book
from .models import Author

def authorBooksBySlug(request, slug):
    author = Author.objects.get(slug=slug)
    books = Book.objects.filter(author__slug=slug).order_by('title')
    context = {
        'author': author,
        'books': books
    }
    return render(request, 'author.html', context)

def listOfAuthors(request):
    letters = 'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    authors = Author.objects.all().order_by('firstname')

    # author model has overrided save method
    # its firstname and lastname after saving change first letter
    # in these fields to upper case by capitalize()
    letterAndAuthors = {}
    for letter in letters:
        letterAndAuthors[letter] = \
        [author for author in authors if str(author.firstname).startswith(letter)]

    # display letters with at least 1 author
    letterAndAuthors = {letter: authors for letter, authors in letterAndAuthors.items() if authors}
    context = {
        'letterAndAuthors': letterAndAuthors
    }
    
    return render(request, 'listOfAuthors.html', context)
