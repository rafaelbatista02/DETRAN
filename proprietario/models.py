from django.db import models

# Create your models here.
class Dono(models.Model):
    nome = models.CharField(max_length=50)
    rg = models.IntegerField()
    cpf = models.IntegerField()
    endereço = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
