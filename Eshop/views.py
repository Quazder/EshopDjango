from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Kategorie, Produkt, Zakaznik, Objednavka, Brand


# home - funkce, která zobrazuje hlavní stránku
def home(request):
    produkty = Produkt.objects.all()
    return render(request, 'hlavni/home.html', {'produkty': produkty})

# Nešel mi brand napojit - takhle jsem otestoval výpis do konzole
# jestli funguje a chyba není v samotném model popřípadě views/urls propojení ale v templatu a url odkazu na něj
#    for produkt in produkty:
#        brand = produkt.brand.all().first()
#       print(f"Brand: {brand}, Brand Name: {brand.nazev if brand else 'No Brand'}")

# PodlahaDetail - funkce, která zobrazuje detail produktu - pk - primární klíč
def PodlahaDetail(request, pk):
    # objects.get(id=pk) - zobrazí produkt podle jeho id
    produkt = Produkt.objects.get(id=pk)
    # render - vyobrazení stránky, v tomhle případě - detail.html, který se nachází v templatech
    return render(request, 'produkt/detail.html', {'produkt': produkt})


def PodlahaKategorie(request, foo):
    # replace - nahradí znak - v tomhle případě - nahradí pomlčku mezerou
    foo = foo.replace('-', ' ')
    # objects.get(nazev=foo) - zobrazí kategorii podle názvu try - pokud se podaří najít kategorii, tak se zobrazí
    # produkty, které patří do této kategorie, jinak se zobrazí zpráva, že kategorie neexistuje a
    # přesměřuje se na hlavni_stranku - home html
    try:
        kategorie = Kategorie.objects.get(nazev=foo)
        produkty = Produkt.objects.filter(kategorie=kategorie)
        return render(request, 'produkt/list.html', {'produkty': produkty, 'kategorie': kategorie})
    except Kategorie.DoesNotExist:
        messages.success(request, "Tahle kategorie neexistuje.")
        return redirect('hlavni_stranka')


def BrandKategorie(request, brand):
    # get the brand
    try:
        brand_instance = Brand.objects.get(nazev=brand)
        produkty = brand_instance.produkt_set.all()
        return render(request, 'produkt/list_brandy.html', {'produkty': produkty, 'brand': brand_instance})
    except Brand.DoesNotExist:
        messages.success(request, "Tahle kategorie neexistuje")
        return redirect('hlavni_stranka')