from . import views

from django.urls import path


urlpatterns = [
    path('buscar/', views.buscar_ano, name='buscar_ano'),
    path('listar/', views.lista_anos, name='lista_ano'),
    path('editar/<int:pk>/', views.editar_ano, name='editar_ano'),
    path('deletar/<int:pk>/', views.deletar_ano, name='deletar_ano'),
    path('', views.home_ano, name='home_ano'),
    
]