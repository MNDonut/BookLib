from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    # path('login/', LoginView.as_view(template_name='', authentication_form=''), name='login'),
    # path('logout/', LogoutView.as_view(template_name=''), name='logout'),
]