from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpResponse
from .forms import HeroiForm
from .models import HeroiModel
import requests

def home(request):
    return render(request, 'home.html')

def cadastro_heroi(request): #Aplicação da API
    if request.method == "POST":
        nome = request.POST.get("nome")
        url = "https://akabab.github.io/superhero-api/api/all.json"
        response = requests.get(url)

        if response.status_code == 200:
            herois_data = response.json()

            # procurar herói pelo nome digitado
            heroi_info = next((h for h in herois_data if h["name"].lower() == nome.lower()), None)

            if heroi_info:
                # criar e salvar objeto no banco
                heroi = HeroiModel(
                    nome = heroi_info["name"],
                    nome_completo = heroi_info.get("biography", {}).get("fullName", "Desconhecido"),
                    editora = heroi_info.get("biography", {}).get("publisher", "Desconhecido"),
                    primeira_aparicao = heroi_info.get("biography", {}).get("firstAppearance", "Desconhecido"),
                    afiliacoes = heroi_info.get("connections", {}).get("groupAffiliation", "Desconhecido"),
                    local_base = heroi_info.get("work", {}).get("base", "Desconhecido"),
                    poder = heroi_info.get("powerstats", {}).get("power", 0),
                    imagem = heroi_info.get("images", {}).get("sm", "")
                )
                heroi.save()
                return redirect("listar_heroi")
            else:
                return HttpResponse("Herói não encontrado na API")
        else: 
            return HttpResponse("Erro ao acessar API")
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
