# Generated by Django 5.0.4 on 2024-04-19 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0039_rename_nazev_produkt_brand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='specifikace',
            new_name='odvetvi',
        ),
    ]
