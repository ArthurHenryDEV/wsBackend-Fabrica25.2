"""
Configuração de URLs para o projeto.

A lista `urlpatterns` roteia URLs para views. Para mais informações, veja:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Exemplos:
Views baseadas em funções
    1. Adicione um import:  from my_app import views
    2. Adicione uma URL ao urlpatterns:  path('', views.home, name='home')
Views baseadas em classes
    1. Adicione um import:  from other_app.views import Home
    2. Adicione uma URL ao urlpatterns:  path('', Home.as_view(), name='home')
Incluindo outra configuração de URL
    1. Importe a função include(): from django.urls import include, path
    2. Adicione uma URL ao urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
