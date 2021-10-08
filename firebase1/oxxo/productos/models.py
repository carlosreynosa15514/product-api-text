from django.db import models

# Create your models here.
class Chela(models.Model):
    marca = models.CharField(max_length=50)
    alcohol = models.DecimalField(max_digits=4, decimal_places=2)
    mililitros = models.IntegerField()
    artesanal = models.BooleanField()
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    editadop = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.marca
        #Sirve para especificar la manera en como va a mostrar los registros
        #en el panel de administracion
        #Aqui solo va a mostrar el nombre de la marca

    # Sigue hacer las migraciones.
        