from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import CartItem, OrderedBook
from book.models import Book, BookRate
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
            # after purchase delete all ordered books from user's cart and reduce their number by 1
            for cartItem in items:
                book = Book.objects.get(ISBN=cartItem.book.ISBN)
                book.number -= 1
                book.save()
                newOrderedBook = OrderedBook.objects.create(
                    orderNumber_id = theSameForm.pk,
                    user = request.user,
                    book = book,
                )
                try:
                    increaseBookRate = BookRate.objects.get(book=book)
                    increaseBookRate.numberOfOrders += 1
                    increaseBookRate.save()
                except BookRate.DoesNotExist:
                    newBookRate = BookRate.objects.create(book=book, numberOfOrders=1)
                    newBookRate.save()
                cartItem.delete()

            return redirect('cart')

        context = {
            'items': items,
            'total': total,
            'form': form
        }

        return render(request, 'cart.html', context)

    # throughout form GET rendering put user's data

    form = OrderForm(
        initial= {
            'userFirstName': request.user.firstname,
            'userLastName': request.user.lastname,
            'userPatronymic': request.user.patronymic,
            'userEmail': request.user.email
        })
        
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