from django.db import models

# Create your models here.

class Estudiante(models.Model):
    
    nombre = models.CharField(max_length=50)  #Campo de caracteres
    apellido = models.CharField(max_length=40)
    curso = models.CharField(max_length=40)
    cumple = models.DateField()  #Campo de Fecha
    edad = models.IntegerField() #Campo de números enteros
    correo = models.EmailField() #Campo de Correo
    adulto = models.BooleanField(default=False)
    
    # "hola"  ----  "profe@coder.com"
    # CharField        EmailField
    
class Profesor(models.Model):
    
    nombre = models.CharField(max_length=40)
    curso = models.CharField(max_length=40)
    dicta = models.BooleanField()