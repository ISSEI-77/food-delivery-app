from django.urls import path
from . import views
# from django.views.generic import TemplateView



urlpatterns = [
    
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
]