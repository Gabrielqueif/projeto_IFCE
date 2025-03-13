from django.shortcuts import render
from .models import insumos, estados, tabela
from rest_framework import viewsets
from ..api.serializers import insumosSerializer, estadosSerializer, tabelaSerializer




def inicio(request):
    return render(
        request,
        'homepage/index.html'
    )


def memorial(request):
    return render(
        request,
        'homepage/memorial.html'
    )


def calculadora(request):
    return render(
        request,
        'homepage/calculadora.html'
    )


def listar_arquivos(request):
    arquivos = insumos.objects.all()
    print(arquivos)  # Adicione esta linha para depuração
    for arquivo in arquivos:
        print(arquivo.classificação, arquivo.codigo_insumo, arquivo.descrição_insumo,
              arquivo.unidade, arquivo.origem_preço)  # Adicione esta linha para depuração
    return render(request, 'homepage/arquivos.html', {'arquivos': arquivos})
