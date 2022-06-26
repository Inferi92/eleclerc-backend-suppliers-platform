# Generated by Django 4.0.4 on 2022-06-26 11:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platform_api', '0006_rename_seles_unit_product_sales_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='ean',
            field=models.BigIntegerField(default=1, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MaxValueValidator(9999999999999), django.core.validators.MinValueValidator(1)]),
        ),
    ]
