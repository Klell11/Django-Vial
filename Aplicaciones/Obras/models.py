from django.db import models

class Carretera(models.Model):
    nombre = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    longitud = models.IntegerField(default=0)
    fecha_fin_estimada = models.DateField()

    def __str__(self):
        return self.nombre
