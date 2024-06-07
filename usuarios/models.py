# usuarios/models.py
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=10)
    #correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
