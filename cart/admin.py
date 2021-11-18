from django.contrib import admin
from cart.models import CartItem, Order, OrderedBook

admin.site.register(Order)
admin.site.register(CartItem)
admin.site.register(OrderedBook)
