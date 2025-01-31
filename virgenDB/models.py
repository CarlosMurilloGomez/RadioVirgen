from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Plan(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return f'ID: {self.id.__str__()} - {self.nombre}'

class Podcast(models.Model):
    nombre = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    categoria = models.CharField(max_length=100)
    fecha_baja = models.DateField(null=True, blank=True)
    likes = models.IntegerField()
    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(categoria__in=['Educativo', 'Comedia', 'Formacion']), name="ch_categoria")
        ]
    def __str__(self):
        return f'ID: {self.id.__str__()} - {self.nombre}'


class Programa(models.Model):
    nombre = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor, related_name='programas')
    def __str__(self):
        return self.nombre



class Familia(models.Model):
    nombre = models.CharField(max_length=100)
    max_miembros = models.IntegerField(default=4)
    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nick = models.CharField(unique=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    fecha_de_baja = models.DateField(null=True, blank=True)
    plan = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name="usuarios", null=True, blank=True)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, related_name="usuarios", null=True, blank=True)
    podcast_pendientes = models.ManyToManyField(Podcast, related_name="usuarios", blank=True)
    me_gusta_podcast = models.ManyToManyField(Podcast, related_name="usuarios", blank=True)
    podcast_reproducciones = models.JSONField(default=dict)

