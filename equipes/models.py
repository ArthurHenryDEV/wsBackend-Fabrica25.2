from django.db import models

class EquipeModel(models.Model):
    nome = models.CharField(max_length=100) # Nome da equipe (obrigatório, máximo de 100 caracteres)
    membros = models.TextField()
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome
