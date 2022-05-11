from operator import truediv
from django.db import models
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
)

# Create your models here.

# TABELA DOS FORNECEDORES
class Fornecedor(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    contribuinte = models.CharField(
        max_length=9,
        null=False,
        blank=False,
        unique=True,
        validators=[
            RegexValidator(r"[1-9]\d*"),
            MinLengthValidator(9),
            MaxLengthValidator(9),
        ],
    )


# TABELA DAS MARCAS
class Marca(models.Model):
    nome = models.CharField(max_length=55, null=False, blank=False)
    fornecedor = models.ForeignKey(
        Fornecedor, on_delete=models.CASCADE, null=False, blank=False
    )

    def __str__(self):
        return self.nome
