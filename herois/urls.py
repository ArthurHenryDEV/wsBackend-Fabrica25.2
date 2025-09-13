from django.contrib import admin
from django.urls import path
from .views import home, cadastro_heroi

urlpatterns = [
    path('', home, name='home'),
    path('cadastro/', cadastro_heroi, name = 'cadastro_heroi'), 
]