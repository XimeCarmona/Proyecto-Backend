from django.urls import path
from funko_api import views

urlpatterns = [
    path('', views.index, name='index_funkos'),
    path('funko_rest/', views.funkos_rest, name='funkos_rest'),
]