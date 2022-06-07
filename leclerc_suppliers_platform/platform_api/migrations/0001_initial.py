# Generated by Django 4.0.4 on 2022-06-06 12:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('name', models.CharField(max_length=55, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('name', models.CharField(choices=[('Branco', 'Branco'), ('Preto', 'Preto'), ('Vermelho', 'Vermelho'), ('Azul', 'Azul'), ('Verde', 'Verde'), ('Amarelo', 'Amarelo'), ('Cinzento', 'Cinzento'), ('Rosa', 'Rosa')], max_length=15, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=8)),
                ('city', models.CharField(max_length=50)),
                ('nif', models.BigIntegerField(primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1)])),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=128, null=True)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('last_login_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ean', models.BigIntegerField(default=1, unique=True, validators=[django.core.validators.MaxValueValidator(9999999999999), django.core.validators.MinValueValidator(1)])),
                ('name', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, max_length=200, null=True)),
                ('recommended_age', models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(199)])),
                ('gross_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
                ('material_type', models.CharField(blank=True, max_length=50, null=True)),
                ('article_dimension', models.CharField(blank=True, max_length=12, null=True)),
                ('box_dimension', models.CharField(blank=True, max_length=12, null=True)),
                ('care_of_use', models.CharField(blank=True, max_length=50, null=True)),
                ('box_content', models.CharField(blank=True, max_length=50, null=True)),
                ('nutriscore', models.CharField(blank=True, max_length=1, null=True)),
                ('ingredients', models.TextField(blank=True, max_length=300, null=True)),
                ('nutritional_table', models.TextField(blank=True, max_length=300, null=True)),
                ('capacity', models.DecimalField(decimal_places=2, max_digits=6)),
                ('capacity_unit', models.CharField(choices=[('gr', 'gramas'), ('kg', 'kilogramas'), ('un', 'unidades'), ('pck', 'packs'), ('caps', 'capsulas'), ('doses', 'doses'), ('lt', 'litros'), ('mm', 'milímetros'), ('cm', 'centímetros'), ('prc', 'porções'), ('saq', 'saquetas')], max_length=5)),
                ('seles_unit', models.CharField(choices=[('un', 'unidade'), ('kg', 'kilograma')], max_length=3)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platform_api.brand')),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='platform_api.color')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platform_api.supplier')),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platform_api.supplier'),
        ),
    ]
