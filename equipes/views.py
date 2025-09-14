from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import EquipeForm
from .models import EquipeModel

def home_equipe(request):
    return render(request, 'home_equipe.html')

def busca_equipe(request):
    if request.method == 'POST':
        form = EquipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro_equipe')
    else: 
        form = EquipeForm()
    return render(request, 'busca_equipe.html', {'form': form})

def lista_equipe(request):
    equipes = EquipeModel.objects.all()
    return render(request, 'lista_equipe.html', {'equipes': equipes})

