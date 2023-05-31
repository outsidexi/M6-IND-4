from django.db import models

class Contenido(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    phone = models.TextField()
    last_name = models.TextField()
    age = models.IntegerField()
    email = models.TextField()

class DatosCliente(models.Model):
    id = models.IntegerField(primary_key=True)
    direccion = models.TextField()
    edad = models.IntegerField()
    profesion = models.TextField()

