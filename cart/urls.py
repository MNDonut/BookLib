from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<str:slug>', views.addCartItem, name='addCartItem'),
    path('remove/<str:slug>', views.removeCartItem, name='removeCartItem')
]