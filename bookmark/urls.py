from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookmarks, name='bookmarks'),
    path('add/<str:slug>/', views.addBookmark, name='addBookmark'),
    path('remove/<str:slug>/', views.removeBookmark, name='removeBookmark')
]