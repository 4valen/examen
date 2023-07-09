from django.db import models

class Region(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'region'
        
class Contact (models.Model):
    nombres = models.CharField(max_length=120)
    apellidos = models.CharField(max_length=120)
    telefono = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'contact'                