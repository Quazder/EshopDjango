from django.shortcuts import render


# Create your views here.
def Kosik(request):
    return render(request, 'hlavni/kosik.html')
