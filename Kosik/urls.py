from django.urls import path

from Kosik import views

# napojení na views, které se nachází v Eshop.views a které obsahují funkce, které se budou zobrazovat na stránce
urlpatterns = [
    path('', views.Kosik, name='kosik_stranka'),

]