from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Familia(models.Model):
    nombre = models.CharField(max_length=100)
    miembros = models.ManyToManyField(Usuario, related_name='familias')
    max_miembros = models.IntegerField(default=4)
    def __str__(self):
        return self.nombre


class Programa(models.Model):
    nombre = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='programas')
    def __str__(self):
        return self.nombre