# Generated by Django 5.0.4 on 2024-04-19 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0038_alter_brand_nazev'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produkt',
            old_name='nazev',
            new_name='brand',
        ),
    ]
