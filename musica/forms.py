from django import forms
from musica.models import Artista, Album, Cancion

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = [
            'titulo',
            'album',
            'artistas',
            'generos',
        ]
