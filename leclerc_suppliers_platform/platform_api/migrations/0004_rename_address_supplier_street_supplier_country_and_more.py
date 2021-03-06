# Generated by Django 4.0.4 on 2022-06-21 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platform_api', '0003_rename_descricao_product_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='address',
            new_name='street',
        ),
        migrations.AddField(
            model_name='supplier',
            name='country',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AddField(
            model_name='supplier',
            name='door_number',
            field=models.CharField(default='-', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='city',
            field=models.CharField(default='-', max_length=50),
        ),
    ]
