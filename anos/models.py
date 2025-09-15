from django.db import models

class AnoModel(models.Model):
    ano = models.IntegerField()
    herois = models.TextField(blank=True)  
    
    def __str__(self):
        return str(self.ano)
    
class Ano(models.Model):
    ano = models.CharField(max_length=10)
    herois = models.TextField() 

    def __str__(self):
        return f"{self.ano} - {self.herois}"