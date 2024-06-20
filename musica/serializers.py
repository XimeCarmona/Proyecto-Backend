from rest_framework import serializers

from musica.models import Artista, Album, Cancion, Genero

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = ('nombre',)

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('nombre', 'artista')

class CancionSerializer(serializers.ModelSerializer):
    album = AlbumSerializer() 
    class Meta:
        model = Cancion
        fields = ('titulo', 'album')

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ('nombre',)