from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Kategorie, Produkt, Zakaznik, Objednavka


def home(request):
    produkty = Produkt.objects.all()
    return render(request, 'hlavni/home.html', {'produkty': produkty})