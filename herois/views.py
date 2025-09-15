import requests  

from .forms import HeroiForm  
from .models import HeroiModel  

from django.shortcuts import render, redirect  
from django.http import HttpResponse  
 
def cadastro_heroi(request): 
    form = HeroiForm()
    if request.method == "POST":  
        nome = request.POST.get("nome")  
        url = "https://akabab.github.io/superhero-api/api/all.json"  
        response = requests.get(url)  
        if response.status_code == 200:  
            herois_data = response.json()  
            heroi_info = next((h for h in herois_data if h["name"].lower() == nome.lower()), None)
            if heroi_info:  
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
        form = HeroiForm()  
    return render(request, 'cadastro_heroi.html', {'form': form})

def editar_heroi(request, pk):
    heroi = HeroiModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = HeroiForm(request.POST, instance=heroi)
        if form.is_valid():
            heroi_editado = form.save(commit=False)
            url = "https://akabab.github.io/superhero-api/api/all.json"
            response = requests.get(url)
            if response.status_code == 200:
                herois_data = response.json()
                heroi_info = next(
                    (h for h in herois_data if heroi_editado.nome.lower() == h["name"].lower()),
                    None
                )
                if heroi_info:
                    heroi_editado.nome_completo = heroi_info.get("biography", {}).get("fullName", "Desconhecido")
                    heroi_editado.editora = heroi_info.get("biography", {}).get("publisher", "Desconhecido")
                    heroi_editado.primeira_aparicao = heroi_info.get("biography", {}).get("firstAppearance", "Desconhecido")
                    heroi_editado.afiliacoes = heroi_info.get("connections", {}).get("groupAffiliation", "Desconhecido")
                    heroi_editado.local_base = heroi_info.get("work", {}).get("base", "Desconhecido")
                    heroi_editado.poder = heroi_info.get("powerstats", {}).get("power", 0)
                    heroi_editado.imagem = heroi_info.get("images", {}).get("sm", "")
                    heroi_editado.save()
                    return redirect('listar_heroi')
                else:
                    form.add_error("nome", "Esse personagem não foi encontrado na API.")
            else:
                form.add_error(None, "Erro ao acessar a API. Tente novamente.")
    else:
        form = HeroiForm(instance=heroi)
    return render(request, 'cadastro_heroi.html', {'form': form})

def deletar_heroi(request, pk):
    heroi = HeroiModel.objects.get(pk=pk)  
    if request.method == 'POST':  
        heroi.delete()  
        return redirect('listar_heroi')  
    return render(request, 'confirmar_delete.html', {'heroi': heroi})

def listar_heroi(request):
    herois = HeroiModel.objects.all()  
    return render(request, 'listar_heroi.html', {'herois' : herois}) 

def home_herois(request):
    return render(request, 'home_herois.html')