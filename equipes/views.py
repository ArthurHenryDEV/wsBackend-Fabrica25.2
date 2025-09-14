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
            return redirect('lista_equipe')
    else: 
        form = EquipeForm()
    return render(request, 'busca_equipe.html', {'form': form})

def lista_equipe(request):
    equipes = EquipeModel.objects.all()

    equipes = EquipeModel.objects.all()
    return render(request, 'lista_equipe.html', {'equipes': equipes})

def deletar_equipe(request, pk):
    equipe = EquipeModel.objects.get(pk=pk)
    if request.method == 'POST':
        equipe.delete()
        return redirect('lista_equipe')
    return render(request, 'confirmar_deletar_equipe.html', {'equipe': equipe})

def editar_equipe(request, pk):
    equipe = EquipeModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = EquipeForm(request.POST, instance=equipe)
        if form.is_valid():
            form.save()
            return redirect('lista_equipe')
    else:
        form = EquipeForm(instance=equipe)
    return render(request, 'busca_equipe.html', {'form': form})