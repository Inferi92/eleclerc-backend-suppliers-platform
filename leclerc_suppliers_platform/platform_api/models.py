from configparser import MAX_INTERPOLATION_DEPTH
from enum import unique
from multiprocessing.sharedctypes import Value
from random import choices
from colorfield.fields import ColorField
from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)

# Create your models here.

# TABELA DOS FORNECEDORES
class Supplier(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    postal_code = models.CharField(max_length=8, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    nif = models.BigIntegerField(
        primary_key=True,
        null=False,
        blank=False,
        unique=True,
        validators=[MaxValueValidator(9999999999), MinValueValidator(1)],
    )
    email = models.EmailField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=128, null=True)
    register_date = models.DateTimeField(auto_now_add=True)
    last_login_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Supplier, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    # # On save, update timestamps
    #     if not self.id:
    #         self.data_registo = timezone.now()
    #     self.data_ultimo_login = timezone.now()
    #     return super(Fornecedor, self).save(*args, **kwargs)


# TABELA DAS MARCAS
class Brand(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False, primary_key=True)
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name


# TABELA DAS CORES
class Color(models.Model):
    COLOR_PALLET = [
        ("Branco","Branco"),
        ("Preto","Preto"),
        ("Vermelho","Vermelho"),
        ("Azul","Azul"),
        ("Verde","Verde"),
        ("Amarelo","Amarelo"),
        ("Cinzento","Cinzento"),
        ("Rosa","Rosa",),
    ]
    name = models.CharField(
        choices=COLOR_PALLET,
        max_length=15,
        unique=True,
        primary_key=True,
    )

    def __str__(self):
        return self.name


# TABELA DOS PRODUTOS
class Product(models.Model):
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, null=False, blank=False
    )
    ean = models.BigIntegerField(
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
    bloqueado = models.BooleanField(default=False, null=False, blank=False)
    descontinuado = models.BooleanField(default=False, null=False, blank=False)
    capacity = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False
    )
    CAPACITY_UN = [
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
        max_length=5, choices=CAPACITY_UN, null=False, blank=False
    )
    SALES_UN = [
        ("un", "unidade"),
        ("kg", "kilograma"),
    ]
    seles_unit = models.CharField(
        max_length=3, choices=SALES_UN, null=False, blank=False
    )

    def __str__(self):
        return self.name
