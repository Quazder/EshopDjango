# Django Eshop

Django Eshop je webový eshop pro prodej podlah. Tento projekt je postaven na Django frameworku.

## Instalace

Následujte tyto kroky pro spuštění projektu na vašem lokálním stroji pro vývoj a testování.

1. Klonujte repozitář:
    ```
    git clone git@github.com:PetrValasek/EshopDjango.git
    ```
2. Přejděte do složky projektu:
    ```
    cd EshopDjango
    ```
3. Vytvořte a aktivujte virtuální prostředí:
    ```
    python -m venv .venv 
    ```
-
    - Linux: source .venv/bin/activate
    - Windows: .venv\Scripts\activate

4. Nainstalujte závislosti:
    ```
    pip install -r requirements.txt
    ```
5. Proveďte migrace databáze:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Spusťte server:
    ```
    python manage.py runserver
    ```
   
Nyní by měl být váš vývojový server spuštěn a dostupný na `http://localhost:8000/cs`