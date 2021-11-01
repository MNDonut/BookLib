from django.shortcuts import render
from .models import Book, Category

def index(request):
    pass

def listOfCategories(request):
    categories = Category.objects.all().order_by('title')
    context = {
        'categories': categories
    }

    return render(request, 'listOfCategories.html', context)

def bookBySlug(request, slug):
    book = Book.objects.get(slug=slug)
    theSameAuthorBooks = Book.objects.filter(author=book.author)
    theSameCategoryBooks = Book.objects.all().order_by('?')[:4]
    context = {
        'book': book,
        'theSameAuthorBooks': theSameAuthorBooks,
        'theSameCategoryBooks': theSameCategoryBooks
    }
    
    return render(request, 'book.html', context)

def booksByCategory(request, slug):
    category  = Category.objects.get(slug=slug)
    books = Book.objects.filter(category=category)
    context = {
        'category': category,
        'books': books
    }

    return render(request, 'booksByCategory.html', context)

def about(request):
    return render(request, 'about.html', {})