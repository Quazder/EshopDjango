from django.urls import path

from Eshop import views
from Eshop.models import Kategorie, Produkt, Zakaznik, Objednavka


urlpatterns = [
    path('cs/', views.home, name='hlavni_stranka'),
    path('cs/<int:pk>', views.PodlahaDetail, name='detail_podlahy'),

]
