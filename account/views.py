from django.shortcuts import render

def register(request):
    context = {}
    return render(request, 'base/base.html', context)
