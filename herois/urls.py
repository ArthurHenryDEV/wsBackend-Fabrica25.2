from django.contrib import admin
from django.urls import path
from .views import home, cadastro_heroi, listar_heroi, editar_heroi

urlpatterns = [
    path('', home, name='home'),
    path('cadastro/', cadastro_heroi, name = 'cadastro_heroi'), 
    path('lista/', listar_heroi, name = 'listar_heroi'),
    path('editar/<int:pk>', editar_heroi, name = 'editar_heroi'),
]