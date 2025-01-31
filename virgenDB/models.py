from django.db import models

# Create your models here.
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