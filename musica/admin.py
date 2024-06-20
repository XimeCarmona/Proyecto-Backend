from django.contrib import admin
from musica.models import Artista, Cancion, Album, Genero

# Register your models here.

admin.site.register(Artista)
admin.site.register(Album)
admin.site.register(Cancion)
admin.site.register(Genero)