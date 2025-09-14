from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import AnoForm
from .models import AnoModel, Ano
import requests


URL = "https://akabab.github.io/superhero-api/api/all.json"

def home_ano(request):
    return render(request, "home_ano.html")

def buscar_ano(request):
    ano_digitado = request.GET.get("ano")
    herois_filtrados = []

    if ano_digitado:
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            for heroi in data:
                aparicao = heroi["biography"]["firstAppearance"]
                if aparicao and ano_digitado in aparicao:
                    herois_filtrados.append({
                        "nome": heroi["name"],
                        "primeira_aparicao": aparicao,
                        "imagem": heroi["images"]["sm"]
                    })

            # salvar no banco apenas os nomes encontrados
            if herois_filtrados:
                nomes = ", ".join([h["nome"] for h in herois_filtrados])
                Ano.objects.create(ano=ano_digitado, herois=nomes)

    return render(request, "lista_ano.html", {
        "ano": ano_digitado,
        "herois": herois_filtrados
    })

def lista_anos(request):
    anos = Ano.objects.all()
    return render(request, "lista_todos_anos.html", {"anos": anos})

def deletar_ano(request, pk):
    registro = get_object_or_404(Ano, pk=pk)
    if request.method == "POST":
        registro.delete()
        return redirect("lista_ano")
    return render(request, "confirmar_delete_ano.html", {"registro": registro})


def editar_ano(request, pk):
    registro = get_object_or_404(Ano, pk=pk)
    if request.method == 'POST':
        form = AnoForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()

            # atualizar heróis do ano
            ano_digitado = form.cleaned_data['ano']
            herois_filtrados = []

            response = requests.get(URL)
            if response.status_code == 200:
                data = response.json()
                for heroi in data:
                    aparicao = heroi["biography"]["firstAppearance"]
                    if aparicao and str(ano_digitado) in aparicao:
                        herois_filtrados.append({
                            "nome": heroi["name"],
                            "primeira_aparicao": aparicao,
                            "imagem": heroi["images"]["xs"]
                        })

                if herois_filtrados:
                    nomes = ", ".join([h["nome"] for h in herois_filtrados])
                    registro.herois = nomes
                    registro.save()

            return redirect('lista_ano')
    else:
        form = AnoForm(instance=registro)

    return render(request, 'editar_ano.html', {'form': form, 'registro': registro})