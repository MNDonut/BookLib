from django.shortcuts import render
from .models import Author

def author(request, slug):
    author = Author.objects.get(slug=slug)
    context = {
        'author': author
    }
    return render(request, 'author.html', context)

def listOfAuthors(request):
    authors = Author.objects.all().order_by('firstname')
    context = {
        'authors': authors
    }
    
    return render(request, 'listOfAuthors.html', context)
