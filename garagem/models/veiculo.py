from django.db import models
from garagem.models import Categoria, Cor, Marca

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="veiculos"
    )
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=True, blank=True
    )

    def __str__(self):
        return f"{self.marca} - {self.categoria} - {self.ano} - {self.cor}"

    class Meta:
        verbose_name = "veículo"
        verbose_name_plural = "veículos"
