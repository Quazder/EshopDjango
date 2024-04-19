# Generated by Django 5.0.4 on 2024-04-19 02:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0009_alter_produkt_material'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produkt',
            name='nazev',
        ),
        migrations.AddField(
            model_name='produkt',
            name='nazev_produktu',
            field=models.ManyToManyField(help_text='Zadejte název produktu', related_name='produkty_nazev', to='Eshop.kategorie', verbose_name='Název produktu'),
        ),
        migrations.AlterField(
            model_name='produkt',
            name='kategorie',
            field=models.ForeignKey(default=1, help_text='Vyberte kategorii produktu', on_delete=django.db.models.deletion.CASCADE, related_name='produkty_kategorie', to='Eshop.kategorie', verbose_name='Kategorie produktu'),
        ),
    ]