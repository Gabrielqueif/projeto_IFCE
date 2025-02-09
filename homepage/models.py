from django.db import models


class insumos(models.Model):
    classificação = models.CharField(max_length=50)
    codigo_insumo = models.IntegerField()
    descrição_insumo = models.TextField()
    unidade = models.CharField(max_length=50)
    origem_preço = models.CharField(max_length=50)
