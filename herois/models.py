from django.db import models

class HeroiModel(models.Model):

    nome = models.CharField(max_length=100)
    nome_completo = models.CharField(max_length=100, null=True, blank=True)
    editora = models.CharField(max_length=100, null=True, blank=True)
    primeira_aparicao = models.CharField(max_length=100, null=True, blank=True)
    afiliacoes = models.CharField(max_length=100, null=True, blank=True)
    local_base = models.CharField(max_length=100,null=True, blank=True)
    poder = models.IntegerField(null=True, blank=True)
    imagem = models.URLField(max_length=300, null=True, blank=True)
    data_criacao = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
