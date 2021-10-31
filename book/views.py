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