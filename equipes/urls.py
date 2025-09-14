from django.urls import path
from .views import busca_equipe, lista_equipe, home_equipe

urlpatterns = [

    path('', home_equipe, name='home_equipe'),
    path('busca/', busca_equipe, name='busca_equipe'),
    path('lista/', lista_equipe, name='lista_equipe'),

]
