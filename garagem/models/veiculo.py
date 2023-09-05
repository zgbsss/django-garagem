from django.db import models
from garagem.models import Acessorio, Cor, Modelo

class Veiculo(models.Model):
    acessorio = models.ForeignKey(Acessorio, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=True, blank=True
    )

    def __str__(self):
        return f"{self.modelo} - {self.ano} - {self.cor}"

    class Meta:
        verbose_name = "veículo"
        verbose_name_plural = "veículos"
