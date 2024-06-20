from django.urls import path
from musica import views

urlpatterns = [
    path('index_musica', views.index_musica, name='index_musica'),
    path('albums/', views.albums_rest, name='albums_rest'),
    path('artista/', views.artistas_rest, name='artista_rest'),
    path('canciones/', views.canciones_rest, name='canciones_rest'),
    path ('new_musica/', views.NewMusicaView.as_view(), name= 'new_musica'),
]
