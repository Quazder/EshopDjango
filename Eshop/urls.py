from django.urls import path

from Eshop import views
from Eshop.models import Kategorie, Produkt, Zakaznik, Objednavka


urlpatterns = [
    path('', views.home, name='hlavni_stranka'),

]
