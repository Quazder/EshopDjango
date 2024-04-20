# Generated by Django 5.0.4 on 2024-04-20 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0041_kategorie_nazev_jednotnecislo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategorie',
            name='nazev_jednotneCislo',
            field=models.CharField(max_length=50, null=True, verbose_name='Název kategorie v jednotném čísle'),
        ),
        migrations.AlterField(
            model_name='kategorie',
            name='popis',
            field=models.TextField(blank=True, default='', max_length=500, null=True, verbose_name='Popis kategorie'),
        ),
    ]