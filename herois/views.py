from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpResponse
from .forms import HeroiForm

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

