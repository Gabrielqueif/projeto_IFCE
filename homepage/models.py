from django.db import models


class insumos(models.Model):

    MATERIAL_CHOICES = [
        ('A', 'Material'),
        ('B', 'Equipamento'),
        ('C', 'Mão de Obra'),
    ]
    ORIGEM_PRECO_CHOICES = [
        ('C', 'C'),
        ('CC', 'CC'),
    ]
    classificação = models.CharField(max_length=1, choices=MATERIAL_CHOICES)
    codigo_insumo = models.IntegerField()
    descrição_insumo = models.TextField()
    unidade = models.CharField(max_length=50)
    origem_preço = models.CharField(
        max_length=2, choices=ORIGEM_PRECO_CHOICES)
