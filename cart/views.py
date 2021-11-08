from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import CartItem
from book.models import Book
from django.http import HttpResponseRedirect

@login_required
def cart(request):
    items = CartItem.objects.filter(user=request.user)
    context = {
        'items': items
    }

    return render(request, 'cart.html', context)

@login_required
def addCartItem(request, slug):
    book = Book.objects.get(slug=slug)
    if CartItem.objects.filter(user=request.user, book=book).exists():
        cartItem = CartItem.objects.get(user=request.user, book=book)
        cartItem.delete()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER")) 

    newcartItem = CartItem.objects.create(user=request.user, book=book)
    newcartItem.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER")) 

@login_required
def removeCartItem(request, slug):
    book = Book.objects.get(slug=slug)
    cartItem = CartItem.objects.get(user=request.user, book=book)
    cartItem.delete()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER")) 