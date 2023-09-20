from django.db import models

# Create your models here.


class Pais(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    continente = models.CharField(max_length=50)
    imagen = models.CharField(max_length=250)

