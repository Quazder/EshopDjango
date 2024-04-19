# Generated by Django 5.0.4 on 2024-04-19 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0018_alter_produkt_barva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkt',
            name='cena',
            field=models.DecimalField(decimal_places=2, default=800, help_text='Zadejte cenu produktu v Kč/m²', max_digits=10, verbose_name='Cena produktu'),
        ),
        migrations.AlterField(
            model_name='produkt',
            name='nazev',
            field=models.CharField(default='', max_length=50, verbose_name='Název produktu'),
        ),
    ]