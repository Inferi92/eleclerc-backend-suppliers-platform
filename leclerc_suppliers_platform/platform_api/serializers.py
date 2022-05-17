from dataclasses import field
from pyexpat import model
from .models import Fornecedor, Marca, Cores, Produto
from rest_framework import serializers


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = "__all__"


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"


class CoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cores
        fields = "__all__"


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
