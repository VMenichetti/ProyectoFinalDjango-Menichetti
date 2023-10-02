from django.db import models

class Pelicula(models.Model):

    nombre = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    imagen = models.ImageField(blank=True , null=True)
    descripcion = models.CharField(max_length=150)
    reseña = models.CharField(max_length=150)
    youtube = models.URLField()

    def _str_(self):
        return f'{self.nombre}'
    
class Serie(models.Model):

    nombre = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    imagen = models.ImageField(blank=True , null=True)
    temporada = models.TextField()
    descripcion = models.CharField(max_length=150)
    reseña = models.CharField(max_length=150)
    youtube = models.URLField()

    def _str_(self):
        return f'{self.nombre}'

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    enlace_web = models.URLField(max_length=200, blank=True)
    imagen = models.ImageField(upload_to='#', blank=True)