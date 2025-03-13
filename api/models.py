from django.db import models

# Create your models here.

class insumos(models.Model):
    classificação = models.CharField(max_length=100)
    codigo_insumo = models.IntegerField()
    descrição_insumo = models.TextField()
    unidade = models.CharField(max_length=50)
    origem_preço = models.CharField(max_length=2)
    def __str__(self):
        return self.descrição_insumo

class estados(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)
    def __str__(self):
        return self.sigla

class tabela(models.Model):
    AC = models.FloatField(null=True)
    AL = models.FloatField(null=True)
    AP = models.FloatField(null=True)
    AM = models.FloatField(null=True)
    BA = models.FloatField(null=True)
    CE = models.FloatField(null=True)
    DF = models.FloatField(null=True)
    ES = models.FloatField(null=True)
    GO = models.FloatField(null=True)
    MA = models.FloatField(null=True)
    MT = models.FloatField(null=True)
    MS = models.FloatField(null=True)
    MG = models.FloatField(null=True)
    PA = models.FloatField(null=True)
    PB = models.FloatField(null=True)
    PR = models.FloatField(null=True)
    PE = models.FloatField(null=True)
    PI = models.FloatField(null=True)
    RJ = models.FloatField(null=True)
    RN = models.FloatField(null=True)
    RS = models.FloatField(null=True)
    RO = models.FloatField(null=True)
    RR = models.FloatField(null=True)
    SC = models.FloatField(null=True)
    SP = models.FloatField(null=True)
    SE = models.FloatField(null=True)
    TO = models.FloatField(null=True) 