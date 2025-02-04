from django.urls import path

from catalog.views import HomePageView
from .views import RegisterView
from django.contrib.auth.views import LoginView, LogoutView
app_name = "users"

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='login.html', next_page='catalog:home'), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:home'), name='logout'),
]