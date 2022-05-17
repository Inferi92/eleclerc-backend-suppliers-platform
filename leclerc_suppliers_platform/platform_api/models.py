from configparser import MAX_INTERPOLATION_DEPTH
from random import choices
from colorfield.fields import ColorField
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
    endereco = models.CharField(max_length=100, null=False, blank=False)
    codigo_postal = models.CharField(max_length=8, null=False, blank=False)
    cidade = models.CharField(max_length=50, null=False, blank=False)
    nif = models.IntegerField(
        null=False,
        blank=False,
        unique=True,
        validators=[
            RegexValidator(r"[1-9]\d*"),
            MinLengthValidator(9),
            MaxLengthValidator(9),
            MaxValueValidator(999999999),
            MinValueValidator(1),
        ],
    )
    email = models.EmailField(max_length=50, null=False, blank=False)
    data_registo = models.DateTimeField(auto_now_add=True)
    data_ultimo_login = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        return self.nome

    # def save(self, *args, **kwargs):
    # # On save, update timestamps
    #     if not self.id:
    #         self.data_registo = timezone.now()
    #     self.data_ultimo_login = timezone.now()
    #     return super(Fornecedor, self).save(*args, **kwargs)


# TABELA DAS MARCAS
class Marca(models.Model):
    nome = models.CharField(max_length=55, null=False, blank=False)
    fornecedor = models.ForeignKey(
        Fornecedor, on_delete=models.CASCADE, null=False, blank=False
    )

    def __str__(self):
        return self.nome


# TABELA DAS CORES
class Cores(models.Model):
    COLOR_PALLET = [
        (
            "#FFFFFF",
            "Branco",
        ),
        (
            "#000000",
            "Preto",
        ),
        (
            "#FF0000",
            "Vermelho",
        ),
        (
            "#0000ff",
            "Azul",
        ),
        (
            "#065535",
            "Verde",
        ),
        (
            "#FFFF00",
            "Amarelo",
        ),
        (
            "#C0C0C0",
            "Cinzento",
        ),
        (
            "#FFC0CB",
            "Rosa",
        ),
    ]
    nome = ColorField(choices=COLOR_PALLET)

    def __str__(self):
        return self.nome


# TABELA DOS PRODUTOS
class Produto(models.Model):
    fornecedor = models.ForeignKey(
        Fornecedor, on_delete=models.CASCADE, null=False, blank=False
    )
    ean = models.IntegerField(
        null=False,
        blank=False,
        unique=True,
        validators=[
            RegexValidator(r"[1-9]\d*"),
            MinLengthValidator(13),
            MaxLengthValidator(13),
            MaxValueValidator(9999999999999),
            MinValueValidator(1),
        ],
    )
    nome = models.CharField(max_length=100, null=False, blank=False)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=False, blank=False)
    descricao = models.TextField(max_length=200, null=True, blank=True)
    idade_recomendada = models.IntegerField(
        null=True,
        blank=False,
        validators=[
            RegexValidator(r"[1-9]\d*"),
            MinLengthValidator(1),
            MaxLengthValidator(3),
            MinValueValidator(1),
            MaxValueValidator(199),
        ],
    )
    cor = models.ForeignKey(Cores, on_delete=models.CASCADE, null=True, blank=False)
    peso_bruto = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False
    )
    tipo_material = models.CharField(max_length=50, null=True, blank=False)
    dimensoes_artigo = models.CharField(max_length=12, null=True, blank=False)
    dimensoes_caixa = models.CharField(max_length=12, null=True, blank=False)
    cuidados_uso = models.CharField(max_length=50, null=True, blank=False)
    conteudo_caixa = models.CharField(max_length=50, null=True, blank=False)
    nutriscore = models.CharField(max_length=1, null=True, blank=False)
    ingredientes = models.TextField(max_length=300, null=True, blank=True)
    tabela_nutricional = models.TextField(max_length=300, null=True, blank=True)
    capacidade = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False
    )
    un_capacidade = [
        ("gr", "gramas"),
        ("kg", "kilogramas"),
        ("un", "unidades"),
        ("pck", "packs"),
        ("caps", "capsulas"),
        ("doses", "doses"),
        ("lt", "litros"),
        ("mm", "milímetros"),
        ("cm", "centímetros"),
        ("prc", "porções"),
        ("saq", "saquetas"),
    ]
    capacidade_un = models.CharField(max_length=5,choices=un_capacidade, null=False, blank=False)
    un_venda = [
        ("un", "unidade"),
        ("kg", "kilograma"),
    ]
    unidade_venda = models.CharField(max_length=3, choices=un_venda, null=False, blank=False)
