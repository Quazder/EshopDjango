from django.contrib import admin
from .models import Kategorie, Produkt, Zakaznik, Objednavka, Brand

# Registrace modelů v administraci Django - vytvoření administrace pro modely| makemigrations a migrate
admin.site.register(Kategorie)
admin.site.register(Brand)
admin.site.register(Produkt)
admin.site.register(Zakaznik)
admin.site.register(Objednavka)
