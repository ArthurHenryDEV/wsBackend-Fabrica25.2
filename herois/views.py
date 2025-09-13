from django.shortcuts import render
from django.http import HttpResponse
from .forms import HeroiForm

def home(request):
    return render(request, 'home.html')

def cadastro_heroi(request):
    contexto = {
        'form': HeroiForm()
    }
    return render(request, 'cadastro_heroi.html', contexto)

