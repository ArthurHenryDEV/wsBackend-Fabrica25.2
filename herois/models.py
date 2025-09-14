from django.db import models  # Importa o módulo de models do Django, usado para criar tabelas no banco de dados

# Define a classe HeroiModel que representa uma tabela no banco de dados
class HeroiModel(models.Model):

    nome = models.CharField(max_length=100)  # Nome do herói (obrigatório, máximo de 100 caracteres)
    nome_completo = models.CharField(max_length=100, null=True, blank=True)  # Nome completo do herói (pode ser nulo ou ficar em branco)
    editora = models.CharField(max_length=100, null=True, blank=True)  # Editora responsável (Marvel, DC etc.) - campo opcional
    primeira_aparicao = models.CharField(max_length=100, null=True, blank=True)  # Primeira aparição em HQs/filmes - campo opcional

    # Afiliações do herói (ex.: Vingadores, Liga da Justiça) - campo opcional
    afiliacoes = models.CharField(max_length=100, null=True, blank=True)

    # Local base do herói (ex.: Nova York, Gotham) - campo opcional
    local_base = models.CharField(max_length=100, null=True, blank=True)

    # Poder numérico (valor inteiro), pode ser nulo
    poder = models.IntegerField(null=True, blank=True)

    # URL de uma imagem do herói (máximo 300 caracteres), pode ser vazio
    imagem = models.URLField(max_length=300, null=True, blank=True)

    # Data de criação do registro (é preenchida automaticamente quando o herói é criado)
    data_criacao = models.DateField(auto_now_add=True)
    
    # Define como o objeto será exibido no admin e em representações de string
    def __str__(self):
        return self.nome
