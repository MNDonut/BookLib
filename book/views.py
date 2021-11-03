from django.shortcuts import render
from edition.models import Edition
from .models import Book, Category
from django.db.models import Count

def index(request):
    top3Editions = Edition.objects.annotate(nb_books=Count('book')).order_by('-nb_books')[:3]
    random4Categories = Category.objects.all().order_by('?')[:4]
    context = {
        'top3Editions': top3Editions,
        'random4Categories': random4Categories
    }
    return render(request, 'index.html', context)

def listOfCategories(request):
    categories = Category.objects.all().order_by('title')
    context = {
        'categories': categories
    }

    return render(request, 'listOfCategories.html', context)

def bookBySlug(request, slug):
    book = Book.objects.get(slug=slug)
    # filter and delete the same book from the queries below
    theSameAuthorBooks = Book.objects.filter(author=book.author).order_by('?').exclude(slug=slug)
    theSameCategoryBooks = Book.objects.all().order_by('?').exclude(slug=slug)[:4]
    context = {
        'book': book,
        'theSameAuthorBooks': theSameAuthorBooks,
        'theSameCategoryBooks': theSameCategoryBooks
    }
    
    return render(request, 'book.html', context)

def bookByCategorySlug(request, slug):
    category  = Category.objects.get(slug=slug)
    books = Book.objects.filter(category=category)
    context = {
        'category': category,
        'books': books
    }

    return render(request, 'booksByCategory.html', context)

def about(request):
    return render(request, 'about.html', {})