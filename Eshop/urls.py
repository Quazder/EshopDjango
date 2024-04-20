from django.urls import path

from Eshop import views
from Eshop.models import Kategorie, Produkt, Zakaznik, Objednavka

# napojení na views, které se nachází v Eshop.views a které obsahují funkce, které se budou zobrazovat na stránce
urlpatterns = [
    path('cs/', views.home, name='hlavni_stranka'),
    path('cs/<int:pk>', views.PodlahaDetail, name='detail_podlahy'),
    path('cs/kategorie/<str:foo>', views.PodlahaKategorie, name='kategorie_podlahy'),
    path('cs/brand/<str:brand>', views.BrandKategorie, name='značka_podlahy'),
]