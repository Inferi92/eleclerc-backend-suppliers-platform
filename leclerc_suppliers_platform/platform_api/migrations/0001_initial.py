# Generated by Django 4.0.4 on 2022-05-17 20:53

import colorfield.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', colorfield.fields.ColorField(choices=[('#FFFFFF', 'Branco'), ('#000000', 'Preto'), ('#FF0000', 'Vermelho'), ('#0000ff', 'Azul'), ('#065535', 'Verde'), ('#FFFF00', 'Amarelo'), ('#C0C0C0', 'Cinzento'), ('#FFC0CB', 'Rosa')], default='#FFFFFF', image_field=None, max_length=18, samples=None)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('codigo_postal', models.CharField(max_length=8)),
                ('cidade', models.CharField(max_length=50)),
                ('nif', models.IntegerField(unique=True, validators=[django.core.validators.RegexValidator('[1-9]\\d*'), django.core.validators.MinLengthValidator(9), django.core.validators.MaxLengthValidator(9), django.core.validators.MaxValueValidator(999999999), django.core.validators.MinValueValidator(1)])),
                ('email', models.EmailField(max_length=50)),
                ('data_registo', models.DateTimeField(auto_now_add=True)),
                ('data_ultimo_login', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=55)),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platform_api.fornecedor')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ean', models.IntegerField(unique=True, validators=[django.core.validators.RegexValidator('[1-9]\\d*'), django.core.validators.MinLengthValidator(13), django.core.validators.MaxLengthValidator(13), django.core.validators.MaxValueValidator(9999999999999), django.core.validators.MinValueValidator(1)])),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, max_length=200, null=True)),
                ('idade_recomendada', models.IntegerField(null=True, validators=[django.core.validators.RegexValidator('[1-9]\\d*'), django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(3), django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(199)])),
                ('peso_bruto', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tipo_material', models.CharField(max_length=50, null=True)),
                ('dimensoes_artigo', models.CharField(max_length=12, null=True)),
                ('dimensoes_caixa', models.CharField(max_length=12, null=True)),
                ('cuidados_uso', models.CharField(max_length=50, null=True)),
                ('conteudo_caixa', models.CharField(max_length=50, null=True)),
                ('nutriscore', models.CharField(max_length=1, null=True)),
                ('ingredientes', models.TextField(blank=True, max_length=300, null=True)),
                ('tabela_nutricional', models.TextField(blank=True, max_length=300, null=True)),
                ('capacidade', models.DecimalField(decimal_places=2, max_digits=6)),
                ('capacidade_un', models.CharField(choices=[('gr', 'gramas'), ('kg', 'kilogramas'), ('un', 'unidades'), ('pck', 'packs'), ('caps', 'capsulas'), ('doses', 'doses'), ('lt', 'litros'), ('mm', 'milímetros'), ('cm', 'centímetros'), ('prc', 'porções'), ('saq', 'saquetas')], max_length=5)),
                ('unidade_venda', models.CharField(choices=[('un', 'unidade'), ('kg', 'kilograma')], max_length=3)),
                ('cor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='platform_api.cores')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platform_api.fornecedor')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platform_api.marca')),
            ],
        ),
    ]
