from django.shortcuts import redirect, render
from .forms import RegistrationForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from cart.models import Order, OrderedBook

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect uses 'login' url, not just render page
            # it'll render CustomLoginForm and you don't have to give it as a parameter in 'render
            return redirect('login')
        else:
            return render(request, 'registration.html', {'form': form})

    form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'registration.html', context)

def logUserOut(request):
    logout(request)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER")) 

def profile(request):
    userOrders = Order.objects.filter(
        userFirstName = request.user.firstname,
        userLastName = request.user.lastname,
        userPatronymic = request.user.patronymic,
        userEmail = request.user.email,
    )
    userOrderedBooks = OrderedBook.objects.filter(user=request.user)
    listOrderAndBooks = []
    for order in userOrders:
        listOrderAndBooks.append(
            {str(order): [orderedBook.book for orderedBook in userOrderedBooks if orderedBook.orderNumber_id==order.orderNumber]}
        )

    context = {
        'listOrderAndBooks': listOrderAndBooks
    }
    
    return render(request, 'profile.html', context)