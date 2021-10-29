from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('category/<str:slug>', views.categoryByName, name='categoryByName'),
    path('categories/', views.listOfCategories, name='listOfCategories'),
    # path('book/<str:slug>')
]