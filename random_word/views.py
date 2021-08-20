from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
datos = {'cuenta': 1, 'palabra':get_random_string(length=14)}

def index(request):
    return render(request,"index.html",datos)

def generar(request):
    datos['cuenta'] += 1
    datos['palabra'] = get_random_string(length=14)
    return redirect('random_word/')

def limpiar(request):
    datos['cuenta'] = 1
    return redirect('random_word/')