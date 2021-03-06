# Generated by Django 4.0.4 on 2022-06-15 16:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('platform_api', '0002_product_bloqueado_product_descontinuado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descricao',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='descontinuado',
            new_name='discontinued',
        ),
        migrations.AddField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
