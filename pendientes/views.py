from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    saludo = "Hola, Mundo! Esta es la raiz /"
    return HttpResponse(saludo) #retornamos el saludo
