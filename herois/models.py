from django.db import models

class HeroiModel(models.Model):

    nome = models.CharField(max_length=100)
    alter_ego = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome


