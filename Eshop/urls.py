from django.urls import path

from Eshop import views
from Eshop.models import Kategorie, Produkt, Zakaznik, Objednavka

# napojení na views, které se nachází v Eshop.views a které obsahují funkce, které se budou zobrazovat na stránce
urlpatterns = [
    path('cs/', views.home, name='hlavni_stranka'),
    # <int:pk> - znamená, že se jedná o číslo (integer) tedy o unikátní identifikátor produktu
    path('cs/<int:pk>', views.PodlahaDetail, name='detail_podlahy'),
    # <str:foo> - znamená, že se jedná o text (string) tedy o název kategorie
    # name='kategorie_podlahy' - pojmenování cesty například pro odkazování na url adresu v templatech
    path('cs/<str:foo>', views.PodlahaKategorie, name='kategorie_podlahy'),

]
