from django.shortcuts import render
from .models import Edition

def edition(request, slug):
    edition = Edition.objects.get(slug=slug)
    context = {
        'edition': edition
    }
    return render(request, 'edition.html', context)

def listOfEditions(request):
    editions = Edition.objects.all().order_by('title')
    context = {
        'editions': editions
    }
    
    return render(request, 'listOfEditions.html', context)
