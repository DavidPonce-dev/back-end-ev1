from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import *

@receiver(post_migrate)
def cargar_datos_iniciales(sender, **kwargs):
    if Pais.objects.count() == 0:
        print("cargando datos iniciales")
        Pais(id=0, nombre="Irlanda", continente="Europa", imagen="/static/img/irlanda.png").save()
        Pais(id=1, nombre="Canadá", continente="América del sur", imagen="/static/img/canada.png").save()
        Pais(id=2, nombre="Argentina", continente="Europa", imagen="/static/img/argentina.png").save()