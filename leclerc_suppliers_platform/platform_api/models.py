from configparser import MAX_INTERPOLATION_DEPTH
from enum import unique
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
class Supplier(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    postal_code = models.CharField(max_length=8, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    nif = models.IntegerField(
        primary_key=True,
        null=False,
        blank=False,
        unique=True,
        validators=[MaxValueValidator(9999999999), MinValueValidator(1)],
    )
    email = models.EmailField(max_length=50, null=False, blank=False)
    register_date = models.DateTimeField(auto_now_add=True)
    last_login_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    # # On save, update timestamps
    #     if not self.id:
    #         self.data_registo = timezone.now()
    #     self.data_ultimo_login = timezone.now()
    #     return super(Fornecedor, self).save(*args, **kwargs)


# TABELA DAS MARCAS
class Brand(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, null=False, blank=False,
    )

    def __str__(self):
        return self.name


# TABELA DAS CORES
class Color(models.Model):
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
    name = ColorField(choices=COLOR_PALLET, unique=True)

    def __str__(self):
        return self.name


# TABELA DOS PRODUTOS
class Product(models.Model):
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, null=False, blank=False
    )
    ean = models.IntegerField(
        null=False,
        blank=False,
        unique=True,
        default=1,
        validators=[
            MaxValueValidator(9999999999999),
            MinValueValidator(1),
        ],
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=False, blank=False)
    descricao = models.TextField(max_length=200, null=True, blank=True)
    recommended_age = models.IntegerField(
        null=True,
        blank=False,
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(199),
        ],
    )
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)
    gross_weight = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=True
    )
    material_type = models.CharField(max_length=50, null=True, blank=True)
    article_dimension = models.CharField(max_length=12, null=True, blank=True)
    box_dimension = models.CharField(max_length=12, null=True, blank=True)
    care_of_use = models.CharField(max_length=50, null=True, blank=True)
    box_content = models.CharField(max_length=50, null=True, blank=True)
    nutriscore = models.CharField(max_length=1, null=True, blank=True)
    ingredients = models.TextField(max_length=300, null=True, blank=True)
    nutritional_table = models.TextField(max_length=300, null=True, blank=True)
    capacity = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False
    )
    capacity_un = [
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
    capacity_unit = models.CharField(
        max_length=5, choices=capacity_un, null=False, blank=False
    )
    seles_un = [
        ("un", "unidade"),
        ("kg", "kilograma"),
    ]
    seles_unit = models.CharField(
        max_length=3, choices=seles_un, null=False, blank=False
    )

    def __str__(self):
        return self.name
