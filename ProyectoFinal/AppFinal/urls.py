from django.urls import path
from AppFinal.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',inicio,name="inicio"),
    path('peliculas/',peliculas, name="peliculas"),
    path('series/',series, name="series"),
    path('usuarios/',usuarios, name="usuarios"),
    path('formulario-pelicula/',formPelicula,name="formularioPelicula"), 
    path('formulario-serie/',formSerie,name="formularioSerie"), 
    path('lista-peliculas/', lista_peliculas, name='ListaPeliculas'),
    path('busqueda-pelicula/',busquedaPelicula,name="BusquedaPelicula"),
    path('buscar/',buscar,name="Buscar"),
    path('error/',error,name="error404"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

