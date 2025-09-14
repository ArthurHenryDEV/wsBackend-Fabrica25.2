from django.urls import path
from django.contrib import admin

from .views import cadastro_heroi, listar_heroi, editar_heroi, deletar_heroi, home_herois

urlpatterns = [
    path('', home_herois, name='home_herois'),
    path('lista/', listar_heroi, name = 'listar_heroi'),
    path('cadastro/', cadastro_heroi, name = 'cadastro_heroi'), 
    path('editar/<int:pk>', editar_heroi, name = 'editar_heroi'),
    path('deletar/<int:pk>', deletar_heroi, name= 'deletar_heroi'),
]