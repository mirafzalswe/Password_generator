
from django.contrib import admin
from django.urls import path, include
from generator import views
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('password/', views.password, name='password')
]
