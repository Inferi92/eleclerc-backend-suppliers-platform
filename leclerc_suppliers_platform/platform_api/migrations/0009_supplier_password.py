# Generated by Django 4.0.4 on 2022-05-25 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platform_api', '0008_alter_brand_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='password',
            field=models.CharField(max_length=128, null=True, verbose_name='password'),
        ),
    ]
