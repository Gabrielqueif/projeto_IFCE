from rest_framework import serializers
from ..homepage.models import insumos, estados, tabela

class insumosSerializer(serializers.ModelSerializer):
    class Meta:
        model = insumos
        fields = '__all__'

class estadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = estados
        fields = '__all__'

class tabelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tabela
        fields = '__all__'