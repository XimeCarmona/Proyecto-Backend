from django.shortcuts import render
from django.http import JsonResponse
from musica.models import Artista, Album, Cancion
from musica.serializers import ArtistaSerializer, AlbumSerializer, CancionSerializer
from django.views.generic import CreateView
from musica.forms import MusicaForm

def index_musica(request):
    artistas = Artista.objects.all()
    albums = Album.objects.all()
    canciones = Cancion.objects.all()
    return render(request, 'index_musica.html', {
        'artistas': artistas,
        'albums': albums,
        'canciones': canciones,
    })

def artistas_rest(request):
    artistas = Artista.objects.all()
    serializer = ArtistaSerializer(artistas, many=True)
    return JsonResponse(serializer.data, safe=False)

def albums_rest(request):
    albums = Album.objects.all()
    serializer = AlbumSerializer(albums, many=True)
    return JsonResponse(serializer.data, safe=False)

def canciones_rest(request):
    canciones = Cancion.objects.all()
    serializer = CancionSerializer(canciones, many=True)
    return JsonResponse(serializer.data, safe=False)

class NewMusicaView(CreateView):
    form_class = MusicaForm
    template_name = 'form_musica.html'
    success_url = '/index_musica/'