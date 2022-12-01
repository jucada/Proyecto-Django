from django.shortcuts import render
from AppCoder.models import Profesor
from django.http import HttpResponse

# Create your views here.

def agregar_profe(request):
    
    
    nuevoProfe = Profesor(nombre="Ernesto", curso="C#", dicta=True)
    nuevoProfe.save()
    
    return HttpResponse("Hemos creado un nuevo profesor.")