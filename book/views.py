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
    # filter and delete the same book from the queries below
    theSameAuthorBooks = Book.objects.filter(author=book.author).exclude(slug=slug)
    theSameCategoryBooks = Book.objects.all().order_by('?').exclude(slug=slug)[:4]
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