from django.apps import AppConfig


# Samo vytvořeno, jedná se o konfiguraci aplikace Eshop, která se napojuje na settings.py,
# aby spolu mohly komunikovat.
class EshopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Eshop'
