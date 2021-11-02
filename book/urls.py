from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<str:slug>', views.bookBySlug, name='bookBySlug'),
    path('categories/', views.listOfCategories, name='listOfCategories'),
    path('category/<str:slug>', views.bookByCategorySlug, name='bookByCategorySlug'),
    path('about/', views.about, name='about'),
]