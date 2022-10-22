from django.db import models

# Create your models here.


class Comuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    rut = models.CharField(max_length=11, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=50)
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    rut = models.CharField(max_length=11)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    

    def __str__(self):
        return self.nombre