from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import CartItem, OrderedBook, Order
from book.models import Book
from django.http import HttpResponseRedirect
from .forms import OrderForm

@login_required
def cart(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(x.book.price for x in items)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            # get instance for using its pk to create new ordered books
            theSameForm = form.save()
            # after purchase delete all ordered books from user's cart and reduce their count by 1
            for cartItem in items:
                book = Book.objects.get(ISBN=cartItem.book.ISBN)
                book.number -= 1
                book.save()
                newOrderedBook = OrderedBook.objects.create(
                    orderNumber_id = theSameForm.pk,
                    user = request.user,
                    book = book,
                )
                cartItem.delete()

            return redirect('index')

        context = {
            'items': items,
            'total': total,
            'form': form
        }

        return render(request, 'cart.html', context)

    form = OrderForm()
    context = {
        'items': items,
        'total': total,
        'form': form
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