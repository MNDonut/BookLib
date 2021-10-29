from django.shortcuts import render
from .models import Book, Category

def index(request):
    pass

def listOfCategories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }

    return render(request, 'listOfCategories.html', context)
