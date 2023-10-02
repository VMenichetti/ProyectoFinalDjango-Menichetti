from django.urls import path
from AppFinal.views import *

urlpatterns = [
    path('',inicio,name="inicio"),
    path('peliculas/',peliculas, name="peliculas"),
    path('series/',series, name="series"),
    path('usuarios/',usuarios, name="usuarios"),
    path('formulario-pelicula/',formPelicula,name="formularioPelicula"), 
    path('formulario-serie/',formSerie,name="formularioSerie"), 
]