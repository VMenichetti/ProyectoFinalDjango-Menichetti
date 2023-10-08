from django.urls import path
from AppFinal.views import *


urlpatterns = [
    path('',inicio,name="inicio"),
    path('peliculas/',peliculas, name="peliculas"),
    path('series/',series, name="series"),
    path('usuarios/',usuarios, name="usuarios"),
    path('formulario-pelicula/',crear_pelicula,name="formularioPelicula"), 
    path('formulario-serie/',formSerie,name="formularioSerie"), 
    path('lista-peliculas/', lista_peliculas, name='ListaPeliculas'),
    path('busqueda-pelicula/',busquedaPelicula,name="BusquedaPelicula"),
    path('buscar/',buscar,name="Buscar"),
    path('error/',error,name="error404"),
    path('eliminarPeliculas/<int:id>', eliminar_pelicula, name="EliminarPeliculas"),
    path('editarPelicula/<int:id>', editar_pelicula, name="EditarPelicula"),
]



