from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views 

urlpatterns = [
     path('', views.home, name='home'),    
    path('contact/', views.contact, name='contact'),
    path('forum/',views.forum, name='forum'),
    path('about/', views.about, name='about'),
    path('rule/', views.rule, name='rule'),
    path('member/', views.members, name='member'),
    path('register/', views.register_request, name="register"),
    path("login/", views.login_request, name="login")
]