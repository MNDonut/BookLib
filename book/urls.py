from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:slug>', views.booksByCategory, name='booksByCategory'),
    path('categories/', views.listOfCategories, name='listOfCategories'),
    # path('book/<str:slug>')
]