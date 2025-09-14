import requests  # Biblioteca para fazer requisições HTTP externas (API)

from .forms import HeroiForm  # Importa o formulário do herói criado em forms.py
from .models import HeroiModel  # Importa o modelo do herói criado em models.py

from django.shortcuts import render, redirect  # Importa funções para renderizar templates e redirecionar URLs
from django.http import HttpResponse  # Importa classes para lidar com requisições e respostas HTTP

 
# Função para cadastrar herói via API
def cadastro_heroi(request): 
    if request.method == "POST":  # Se o formulário foi enviado
        nome = request.POST.get("nome")  # Pega o valor do campo "nome" enviado pelo usuário

        url = "https://akabab.github.io/superhero-api/api/all.json"  # URL da API de heróis
        response = requests.get(url)  # Faz uma requisição GET para obter todos os heróis

        if response.status_code == 200:  # Se a requisição foi bem-sucedida
            herois_data = response.json()  # Converte a resposta JSON em uma lista de dicionários

            # Procura o herói na lista que tem o mesmo nome digitado (case insensitive)
            heroi_info = next((h for h in herois_data if h["name"].lower() == nome.lower()), None)

            if heroi_info:  # Se encontrou o herói
                # Cria um objeto HeroiModel preenchendo os campos com dados da API
                heroi = HeroiModel(
                    nome = heroi_info["name"],  # Nome do herói
                    nome_completo = heroi_info.get("biography", {}).get("fullName", "Desconhecido"),  # Nome completo ou "Desconhecido"
                    editora = heroi_info.get("biography", {}).get("publisher", "Desconhecido"),  # Editora
                    primeira_aparicao = heroi_info.get("biography", {}).get("firstAppearance", "Desconhecido"),  # Primeira aparição
                    afiliacoes = heroi_info.get("connections", {}).get("groupAffiliation", "Desconhecido"),  # Afiliacoes / equipes
                    local_base = heroi_info.get("work", {}).get("base", "Desconhecido"),  # Local base
                    poder = heroi_info.get("powerstats", {}).get("power", 0),  # Poder (valor numérico)
                    imagem = heroi_info.get("images", {}).get("sm", "")  # URL da imagem pequena
                )
                heroi.save()  # Salva o objeto no banco de dados
                return redirect("listar_heroi")  # Redireciona para a lista de heróis
            else:
                return HttpResponse("Herói não encontrado na API")  #   Resposta caso não encontre o herói
        else: 
            return HttpResponse("Erro ao acessar API")  # Caso a API não responda corretamente (esteja fora do ar, etc)
    else:
        form = HeroiForm()  # Se for GET, apenas cria o formulário vazio
    return render(request, 'cadastro_heroi.html', {'form': form})  # Renderiza o template com o formulário

# Função para editar herói já cadastrado
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
                    # heroi_editado atualiza os dados com as informações da API
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
                    # Se não achou o herói na API -> adiciona erro no campo "nome"
                    form.add_error("nome", "Esse personagem não foi encontrado na API.")
            else:
                form.add_error(None, "Erro ao acessar a API. Tente novamente.")
    else:
        form = HeroiForm(instance=heroi)

    return render(request, 'cadastro_heroi.html', {'form': form})

# Função para deletar herói
def deletar_heroi(request, pk):
    heroi = HeroiModel.objects.get(pk=pk)  # Busca herói pelo ID
    if request.method == 'POST':  # Se confirmou exclusão
        heroi.delete()  # Deleta o herói do banco
        return redirect('listar_heroi')  # Redireciona para lista de heróis
    return render(request, 'confirmar_delete.html', {'heroi': heroi})

# Função para listar todos os heróis cadastrados
def listar_heroi(request):
    herois = HeroiModel.objects.all()  # Pega todos os heróis do banco
    return render(request, 'listar_heroi.html', {'herois' : herois})  # Renderiza template com lista

def home_herois(request):
    return render(request, 'home_herois.html')