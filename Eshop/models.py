from django.db import models


# Create your models here.

# Create a model for the product

class Kategorie(models.Model):
    nazev = models.CharField(max_length=50, verbose_name='Název kategorie',help_text='Vytvořte novou kategorii' , unique=True)

    class Meta:
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorie'

    def __str__(self):
        return self.nazev


class Produkt(models.Model):
    nazev = models.CharField(max_length=50, verbose_name='Název produktu', unique=True)
    cena = models.DecimalField(default=0, decimal_places=2, max_digits=10, verbose_name='Cena produktu', help_text='Zadejte cenu prodoktu v kč')
    kategorie = models.ForeignKey(Kategorie, on_delete=models.CASCADE, default=1, verbose_name='Kategorie produktu', help_text='Vyberte kategorii produktu')
    popis = models.CharField(max_length=500, default='', blank=True, null=True, verbose_name='Popis produktu', help_text='Zadejte popis produktu - max 500 znaků')
    fotka = models.ImageField(upload_to='fotky/produkty/', verbose_name='Fotka produktu', help_text='Vyberte fotku produktu')
    je_akce = models.BooleanField(default=False, verbose_name='Je produkt v akci', help_text='Zaškrtněte pokud je produkt v akci')
    akce_cena = models.DecimalField(default=0, decimal_places=2, max_digits=10, verbose_name='Akční cena', help_text='Zadejte akční cenu produktu v kč')

    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'

    def __str__(self):
        return f'{self.nazev} - {self.cena} Kč'


class Zakaznik(models.Model):
    jmeno = models.CharField(max_length=50, verbose_name='Jméno', help_text='Zadejte jméno zakazníka')
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení', help_text='Zadejte příjmení zakazníka')
    telefon = models.CharField(max_length=20, verbose_name='Telefon', help_text='Zadejte telefonní číslo zakazníka', default='', blank=True)
    email = models.EmailField(max_length=100, verbose_name='Email', help_text='Zadejte email zakazníka', unique=True)
    heslo = models.CharField(max_length=50, verbose_name='Heslo', help_text='Zadejte heslo')

    class Meta:
        verbose_name = 'Zakaznik'
        verbose_name_plural = 'Zakaznici'

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'


class Objednavka(models.Model):
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE, verbose_name='Produkt', help_text='Vyberte produkt')
    zakaznik = models.ForeignKey(Zakaznik, on_delete=models.CASCADE, verbose_name='Zakaznik', help_text='Vyberte zakazníka')
    pocet = models.IntegerField(default=1, verbose_name='Počet', help_text='Zadejte počet produktů')
    adresa = models.CharField(max_length=100, default='', blank=True, verbose_name='Adresa', help_text='Zadejte adresu zakazníka')
    telefon = models.CharField(max_length=20, default='', blank=True, verbose_name='Telefon', help_text='Zadejte telefonní číslo zakazníka')
    # auto_now_add=True - automaticky se nastavi datum na aktualni datum
    datum = models.DateField(auto_now_add=True, verbose_name='Datum', help_text='Datum objednávky')
    status = models.BooleanField(default=False, verbose_name='Stav', help_text='Zaškrtněte pokud je objednávka vyřízena')

    class Meta:
        verbose_name = 'Objednavka'
        verbose_name_plural = 'Objednavky'

    def __str__(self):
        return f'{self.produkt} - {self.zakaznik} - {self.datum}'
