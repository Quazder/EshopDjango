from django.contrib import admin
from .models import Kategorie, Produkt, Zakaznik, Objednavka
# Registrace modelů v administraci Django - vytvoření administrace pro modely
admin.site.register(Kategorie)
admin.site.register(Produkt)
admin.site.register(Zakaznik)
admin.site.register(Objednavka)