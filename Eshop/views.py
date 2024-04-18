from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Kategorie, Produkt, Zakaznik, Objednavka


def home(request):
    produkty = Produkt.objects.all()
    return render(request, 'hlavni/home.html', {'produkty': produkty})


def PodlahaDetail(request, pk):
    produkt = Produkt.objects.get(id=pk)
    return render(request, 'produkt/detail.html', {'produkt': produkt})


def PodlahaKategorie(request, foo):
    foo = foo.replace('-', ' ')
    try:
        kategorie = Kategorie.objects.get(nazev=foo)
        produkty = Produkt.objects.filter(kategorie=kategorie)
        return render(request, 'produkt/list.html', {'produkty': produkty, 'kategorie': kategorie})
    except:
        messages.success(request, ("Tahle kategorie neexistuje."))
        return redirect('hlavni_stranka')
