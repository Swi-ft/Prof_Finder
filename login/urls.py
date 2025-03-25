from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view
from django.contrib import admin

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name ='signup'),
    path('home/', views.home, name = "home"),
    path('mailing/', views.mailing, name="mailing"),
    path("generate_mail/", views.generate_mail, name="generate_mail"),
]  
