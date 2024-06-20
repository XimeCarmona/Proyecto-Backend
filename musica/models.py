from django.db import models

# Create your models here.

class Artista(models.Model):
    nombre = models.CharField(max_length=128)
    fechaNac = models.DateField()

    def __str__(self):
        return self.nombre

class Album(models.Model):
    nombre = models.CharField(max_length=128)
    fechaLanzamiento = models.DateField()
    artista = models.ForeignKey(Artista, related_name='albums', on_delete=models.PROTECT) 
    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre

class Cancion(models.Model):
    titulo = models.CharField(max_length=128)
    duracion = models.DurationField()
    album = models.ForeignKey(Album, on_delete=models.PROTECT)  
    artistas = models.ManyToManyField(Artista, blank=True) 
    generos = models.ManyToManyField(Genero, blank=True) 

    def __str__(self):
        return self.titulo
