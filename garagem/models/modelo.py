from django.db import models
from garagem.models import Categoria, Marca

class Modelo(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="modelos")
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="modelos")
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao