from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import BookMark
from book.models import Book

def bookmarks(request):
    bookmarks = BookMark.objects.filter(user=request.user)
    context = {
        'bookmarks': bookmarks
    }

    return render(request, 'bookmarks.html', context)

def addBookmark(request, slug):
    book = Book.objects.get(slug=slug)
    if BookMark.objects.filter(user=request.user, book=book).exists():
        bookMark = BookMark.objects.get(user=request.user, book=book)
        bookMark.delete()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER")) 

    newBookMark = BookMark.objects.create(user=request.user, book=book)
    newBookMark.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER")) 

def removeBookmark(request, slug):
    book = Book.objects.get(slug=slug)
    bookMark = BookMark.objects.get(user=request.user, book=book)
    bookMark.delete()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER")) 