from django.urls import path
from . import views

urlpatterns = [
    path('', views.listOfEditions, name='listOfEditions'),
    path('<str:slug>/', views.edition, name='edition')
]