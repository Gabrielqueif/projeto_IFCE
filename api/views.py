from django.shortcuts import render
from .models import insumos, estados, tabela
from .serializers import insumosSerializer, estadosSerializer, tabelaSerializer
from rest_framework import viewsets

# Create your views here.
class insumosviewset(viewsets.ModelViewSet):
    queryset = insumos.objects.all()
    serializer_class = insumosSerializer

class estadosviewset(viewsets.ModelViewSet):
    queryset = estados.objects.all()
    serializer_class = estadosSerializer

class tabelaviewset(viewsets.ModelViewSet):
    queryset = tabela.objects.all()
    serializer_class = tabelaSerializer