from django.urls import path

from Eshop import views
from Eshop.models import Kategorie, Produkt, Zakaznik, Objednavka

# napojení na views, které se nachází v Eshop.views a které obsahují funkce, které se budou zobrazovat na stránce
urlpatterns = [
    path('', views.home, name='hlavni_stranka'),
    path('<int:pk>', views.PodlahaDetail, name='detail_podlahy'),
    path('kategorie/<str:foo>', views.PodlahaKategorie, name='kategorie_podlahy'),
    path('brand/<str:brand>', views.BrandKategorie, name='značka_podlahy'),
    path('přihlášení/', views.prihlaseni_uzivatele, name='prihlaseni'),
    path('registrace/', views.registrace_uzivatele, name='registrace'),
    path('odhlášení/', views.odhlaseni_uzivatele, name='odhlaseni'),
    path('zmena_hesla/', views.zmena_hesla, name='zmena_hesla'),
    path('zmena_profilu/', views.zmena_profilu, name='zmena_profilu'),
    path('produkt/<int:product_id>/add_recenze/', views.add_recenze, name='add_recenze'),
    path('delete_recenze/<int:recenze_id>/', views.delete_recenze, name='delete_recenze'),
]
