from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .forms import SignUpForm, EditProfileForm, RecenzeForm
from .models import Kategorie, Produkt, Zakaznik, Objednavka, Brand, Recenze


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
    produkt = Produkt.objects.get(id=pk)
    recenze = Recenze.objects.filter(produkt=produkt)
    form = RecenzeForm()
    return render(request, 'produkt/detail.html', {'produkt': produkt, 'recenze': recenze, 'form': form})


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


def prihlaseni_uzivatele(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Přihlášení proběhlo úspěšně.")
            return redirect('hlavni_stranka')
        else:
            messages.success(request, "Operace se nezdařila, prosím, zkuste to znovu.")
            return redirect('prihlaseni')

    else:
        return render(request, 'uzivatele/login.html')


def registrace_uzivatele(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registrace proběhla úspěšně.")
            return redirect('hlavni_stranka')
        else:
            messages.success(request, "Operace se nezdařila, prosím, zkuste to znovu.")
            return redirect('registrace')
    else:
        return render(request, 'uzivatele/registrace.html', {'form': form})


def odhlaseni_uzivatele(request):
    logout(request)
    messages.success(request, "Odhlášení proběhlo úspěšně.")
    return redirect('hlavni_stranka')


def zmena_hesla(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Změnili jste Vaše heslo.')
            return redirect('hlavni_stranka')
    else:
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}
    return render(request, 'uzivatele/zmenit_heslo.html', context)


def zmena_profilu(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Změnili jste Váš profil')
            return redirect('hlavni_stranka')
    else:
        form = EditProfileForm(instance=request.user)

    context = {'form': form}
    return render(request, 'uzivatele/zmenit_profil.html', context)


def add_recenze(request, product_id):
    produkt = get_object_or_404(Produkt, pk=product_id)
    if request.method == "POST":
        form = RecenzeForm(request.POST)
        if form.is_valid():
            recenze = form.save(commit=False)
            recenze.user = request.user
            recenze.produkt = produkt
            recenze.save()
    return redirect('detail_podlahy', pk=produkt.id)
