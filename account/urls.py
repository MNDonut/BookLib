from django.urls import path
from account.forms import CustomLoginForm
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html', authentication_form=CustomLoginForm), name='login'),
    # define my view to refresh the page after logout
    path('logout/', views.logUserOut, name='logout'),
]