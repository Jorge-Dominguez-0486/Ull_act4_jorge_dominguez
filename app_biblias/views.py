from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    productos_biblias = [
        {"nombre": "Biblia de Estudio NVI", "precio": "€35.99", "editorial": "Vida"},
        {"nombre": "Biblia RVR 1960 Letra Grande", "precio": "€28.50", "editorial": "Nelson"},
        {"nombre": "Biblia Bilingüe (Español-Inglés)", "precio": "€42.00", "editorial": "Zondervan"},
    ]
    context = {
        'productos': productos_biblias
    }
    return render(request, 'index.html', context)