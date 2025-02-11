from django.db import models

# Modelo Carretera
class Carretera(models.Model):
    nombre = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=500)
    longitud = models.FloatField()
    fecha_fin_estimada = models.DateField()

    def __str__(self):
        return self.nombre

# Modelo Constructora
class Constructora(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=500)
    telefono = models.CharField(max_length=20)
    representante = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Presupuesto(models.Model):
    nombre = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


# Modelo Proyecto
class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    constructora = models.ForeignKey(Constructora, on_delete=models.CASCADE)
    presupuesto = models.ForeignKey(Presupuesto, on_delete=models.CASCADE)
    carretera = models.ForeignKey(Carretera, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre