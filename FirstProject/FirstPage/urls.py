from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.Home, name = "Home"),
    path('Register/', views.Register, name = "Register"),
    path('ForgotPassword/', views.ForgotPassword, name = "ForgotPassword"),
    path('Number_of_Companies/', views.Number_of_Companies, name = "Number_of_Companies"),
    path('List_of_Companies/', views.List_of_Companies, name = "List_of_Companies"),
    path('logout/', views.logoutUser, name = "logout"),
]
