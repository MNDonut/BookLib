from django.urls import path
from . import views

urlpatterns = [
    path('', views.listOfAuthors, name='listOfAuthors'),
    path('<str:slug>/', views.authorBooksBySlug, name='authorBooksBySlug')
]