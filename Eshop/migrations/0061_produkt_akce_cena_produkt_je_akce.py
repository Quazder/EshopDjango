# Generated by Django 5.0.4 on 2024-04-22 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Eshop", "0060_recenze_hodnoceni"),
    ]

    operations = [
        migrations.AddField(
            model_name="produkt",
            name="akce_cena",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                help_text="Zadejte akční cenu produktu v kč/m³",
                max_digits=10,
                verbose_name="Akční cena",
            ),
        ),
        migrations.AddField(
            model_name="produkt",
            name="je_akce",
            field=models.BooleanField(
                default=False,
                help_text="Zaškrtněte pokud je produkt v akci",
                verbose_name="Je produkt v akci",
            ),
        ),
    ]