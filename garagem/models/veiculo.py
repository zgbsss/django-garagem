from django.db import models
from garagem.models import Acessorio, Cor, Modelo
from uploader.models import Image

class Veiculo(models.Model):
    acessorio = models.ManyToManyField(Acessorio, related_name="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    descricao = models.CharField(max_length=100, null=True, blank=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=True, blank=True
    )
    capa = models.ManyToManyField(Image, related_name="+")

    def __str__(self):
        return f"{self.modelo} - {self.ano} - {self.cor}"

    class Meta:
        verbose_name = "veículo"
        verbose_name_plural = "veículos"
