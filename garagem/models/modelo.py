from django.db import models

class Modelo(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao