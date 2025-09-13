from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpResponse
from .forms import HeroiForm
from .models import HeroiModel

def home(request):
    return render(request, 'home.html')

def cadastro_heroi(request):
    if request.method == "POST":
        form = HeroiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = HeroiForm()
    return render(request, 'cadastro_heroi.html', {'form': form})

def listar_heroi(request):
    herois = HeroiModel.objects.all()
    return render(request, 'listar_heroi.html', {'herois' : herois})

def editar_heroi(request, pk):
    heroi = HeroiModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = HeroiForm(request.POST, instance=heroi)
        if form.is_valid():
            form.save()
            return redirect('listar_heroi')
    else:
        form = HeroiForm(instance=heroi)
    return render(request, 'cadastro_heroi.html', {'form': form})

def deletar_heroi(request, pk):
    heroi = HeroiModel.objects.get(pk=pk)
    if request.method == 'POST':
        heroi.delete()
        return redirect ('listar_heroi')
    return render(request, 'confirmar_delete.html', {'heroi': heroi})
