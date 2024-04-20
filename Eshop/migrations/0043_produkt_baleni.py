# Generated by Django 5.0.4 on 2024-04-20 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0042_alter_kategorie_nazev_jednotnecislo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkt',
            name='baleni',
            field=models.DecimalField(decimal_places=2, default=1, help_text='Zadejte počet metrů čtverečních v balení', max_digits=10, verbose_name='Obsah balení'),
        ),
    ]