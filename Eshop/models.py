from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# modely pro eshop - 5 modelů - Kategorie, Brand, Produkt, Zakaznik, Objednavka
class Kategorie(models.Model):
    nazev = models.CharField(max_length=50, verbose_name='Název kategorie', help_text='Vytvořte novou kategorii',
                             unique=True)
    nazev_jednotneCislo = models.CharField(max_length=50, verbose_name='Název kategorie v jednotném čísle', null=True)
    popis = models.TextField(max_length=500, default='', blank=True, null=True, verbose_name='Popis kategorie')

    class Meta:
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorie'

    def __str__(self):
        return self.nazev


class Brand(models.Model):
    BRAND_CHOICES = [
        ('nizza', 'Nizza'),
        ('zen', 'Zen'),
        ('dublin', 'Dublin'),
        ('kahrs', 'Kahrs'),
        ('triumph', 'Triumph'),
        ('soldline', 'Soldline'),
    ]

    SPECIFIKACE_CHOICES = [
        ('', ''),
        ('koberce', 'Koberec'),
        ('vinyl', 'Vinylové podlahy'),
        ('drevo', 'Dřevěné podlahy'),
        ('laminat', 'Laminátové podlahy'),
    ]

    nazev = models.CharField(max_length=50, verbose_name='Jméno brandu', choices=BRAND_CHOICES)
    popis = models.CharField(max_length=500, default='', verbose_name='Popis brandu')
    odvetvi = models.CharField(max_length=50, verbose_name='Specifikace', choices=SPECIFIKACE_CHOICES, default='')

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brandy'

    def __str__(self):
        if self.nazev is None:
            return 'No brand name'
        else:
            return self.nazev.capitalize()


class Produkt(models.Model):
    BARVA_CHOICES = [
        ('', ''),
        ('černá', 'Černá'),
        ('světlá', 'Světlá'),
        ('hnědá', 'Hnědá'),
        ('šedá', 'Šedá'),
        ('světle šedá', 'Světle šedá'),
        ('tmavě šedá', 'Tmavě šedá'),
        ('béžová', 'Béžová'),
        ('světle béžová', 'Světle béžová'),
        ('akátová', 'Akátová'),

    ]

    MATERIAL_CHOICES = [
        (' ', ' '),
        ('dub', 'Dub'),
        ('buk', 'Buk'),
        ('smrk', 'Smrk'),
        ('javor', 'Javor'),
        ('bříza', 'Bříza'),
        ('jedle', 'Jedle'),
        ('borovice', 'Borovice'),
        ('akát', 'Akát'),
        ('mahagon', 'Mahagon'),
        ('bambus', 'Bambus'),
        ('jasan', 'Jasan'),
    ]
    # max_length - maximální délka textu
    # verbose_name - název sloupce v administraci
    # unique - hodnota musí být unikátní
    brand = models.ManyToManyField(Brand, verbose_name='Název produktu', help_text='Brand = název produktu')
    # ForeignKey - vazba na jiný model - v tomto případě na model Kategorie
    # on_delete=models.CASCADE - pokud se smaže kategorie, smaže se i všechny produkty v této kategorii
    kategorie = models.ForeignKey(Kategorie, on_delete=models.CASCADE, default=1, verbose_name='Kategorie produktu',
                                  help_text='Vyberte kategorii produktu')

    barva = models.CharField(max_length=50, verbose_name='Barva', choices=BARVA_CHOICES, blank='True')
    material = models.CharField(max_length=50, verbose_name='Materiál', choices=MATERIAL_CHOICES,
                                blank='True')

    # decimal_places - počet desetinných míst
    # max_digits - maximální počet číslic
    # default - výchozí hodnota
    # help_text - nápověda - zobrazí se v administraci vedle pole
    cena = models.PositiveIntegerField(verbose_name='Cena produktu',
                                       help_text='Zadejte cenu produktu v Kč/m² - Pouze u podlah| Ostatně Kč/ks')
    baleni = models.DecimalField(default=1, verbose_name='Obsah balení', decimal_places=2, max_digits=10,
                                 help_text='Zadejte počet metrů čtverečních v balení',
                                 validators=[MinValueValidator(0.1), MaxValueValidator(7)])

    # CharField - textové pole
    # blank=True - pole může být prázdné
    # null=True - hodnota může být null
    popis = models.CharField(max_length=500, default='', blank=True, null=True, verbose_name='Popis produktu',
                             help_text='Zadejte popis produktu - max 500 znaků')

    # ImageField - obrázek/fotka/logo...
    # upload_to - cesta kam se uloží fotka produktu - media/fotky/produkty
    fotka = models.ImageField(upload_to='fotky/produkty/', verbose_name='Fotka produktu',
                              help_text='Vyberte fotku produktu')

    closeup_fotka = models.ImageField(upload_to='fotky/closeup/', verbose_name='Fotka produktu v bytě',
                                      help_text='Vyberte fotku z dálky', blank=True)

    # BooleanField - True/False
    # default=False - výchozí hodnota Booleanu je False
    je_akce = models.BooleanField(default=False, verbose_name='Je produkt v akci',
                                  help_text='Zaškrtněte pokud je produkt v akci')

    # DecimalField - desetinné číslo
    akce_cena = models.DecimalField(default=0, decimal_places=2, max_digits=10, verbose_name='Akční cena',
                                    help_text='Zadejte akční cenu produktu v kč/m³')

    # Meta - vlastnosti modelu
    # verbose_name - název modelu v jednotném čísle
    # verbose_name_plural - název modelu v množném čísle
    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'

    # __str__ - metoda, která se volá při výpisu objektu - v administraci
    # vrací název produktu a cenu produktu v Kč
    def __str__(self):
        brand_names = ", ".join([str(brand) for brand in self.brand.all()])
        return f'| {brand_names} | {self.cena} Kč/m³ | {self.kategorie} | {self.baleni}m² |'


class Zakaznik(models.Model):
    jmeno = models.CharField(max_length=50, verbose_name='Jméno', help_text='Zadejte jméno zakazníka')
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení', help_text='Zadejte příjmení zakazníka')
    telefon = models.CharField(max_length=20, verbose_name='Telefon', help_text='Zadejte telefonní číslo zakazníka',
                               default='', blank=True)
    email = models.EmailField(max_length=100, verbose_name='Email', help_text='Zadejte email zakazníka', unique=True)
    heslo = models.CharField(max_length=50, verbose_name='Heslo', help_text='Zadejte heslo')

    class Meta:
        verbose_name = 'Zakaznik'
        verbose_name_plural = 'Zakaznici'

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'


class Objednavka(models.Model):
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE, verbose_name='Produkt', help_text='Vyberte produkt')
    zakaznik = models.ForeignKey(Zakaznik, on_delete=models.CASCADE, verbose_name='Zakaznik',
                                 help_text='Vyberte zakazníka')
    pocet = models.IntegerField(default=1, verbose_name='Počet', help_text='Zadejte počet produktů')
    adresa = models.CharField(max_length=100, default='', blank=True, verbose_name='Adresa',
                              help_text='Zadejte adresu zakazníka')
    telefon = models.CharField(max_length=20, default='', blank=True, verbose_name='Telefon',
                               help_text='Zadejte telefonní číslo zakazníka')
    # auto_now_add=True - automaticky se nastavi datum na aktualni datum
    datum = models.DateField(auto_now_add=True, verbose_name='Datum', help_text='Datum objednávky')
    status = models.BooleanField(default=False, verbose_name='Stav',
                                 help_text='Zaškrtněte pokud je objednávka vyřízena')

    class Meta:
        verbose_name = 'Objednavka'
        verbose_name_plural = 'Objednavky'

    def __str__(self):
        return f'{self.produkt} - {self.zakaznik} - {self.datum}'


class Recenze(models.Model):
    HODNOCENI_CHOICES = [
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    text = models.TextField()
    datum = models.DateTimeField(auto_now_add=True)
    hodnoceni = models.IntegerField(choices=HODNOCENI_CHOICES, default=5,
                                    validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        verbose_name = 'Recenze'
        verbose_name_plural = 'Recenze'

    def __str__(self):
        return f'{self.produkt} ---> {self.user} | {self.hodnoceni} hodnoceni'
