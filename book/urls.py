from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<str:slug>', views.booksByCategory, name='booksByCategory'),
    path('categories/', views.listOfCategories, name='listOfCategories'),
    # path('book/<str:slug>')
]