from django.urls import path
from .views import busca_equipe, lista_equipe, home_equipe, deletar_equipe, editar_equipe

urlpatterns = [

    path('', home_equipe, name='home_equipe'),
    path('busca/', busca_equipe, name='busca_equipe'),
    path('lista/', lista_equipe, name='lista_equipe'),
    path('deletar/<int:pk>', deletar_equipe, name='confirmar_deletar_equipe'),
    path('editar/<int:pk>', editar_equipe, name='editar_equipe'),

]
