from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import *
from .forms import FormPelicula,FormSerie

def inicio(req):
    return render(req, "inicio.html")

def peliculas(req):
    return render(req, "peliculas.html")

def series(req):
    return render(req, "inicio.html")

def usuarios(req):
    return render(req, "inicio.html")

# FORMULARIOS

def formPelicula(req):
    print('method',req.method)
    print('POST',req.POST)

    if req.method == 'POST':
        miFormulario=FormPelicula(req.POST)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            pelicula=Pelicula(nombre=data['nombre'],subtitulo=data['subtitulo'],imagen=data['imagen'],descripcion=data['descripcion'],reseña=data['reseña'],youtube=data['youtube'])
            pelicula.save()

        return render(req,"formPelicula.html")
    
    else:
        miFormulario=FormPelicula()
        return render(req, "formPelicula.html",{"miFormulario":miFormulario})

def formSerie(req):
    print('method',req.method)
    print('POST',req.POST)

    if req.method == 'POST':
        miFormulario=FormSerie(req.POST)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            serie=Serie(nombre=data['nombre'],subtitulo=data['subtitulo'],imagen=data['imagen'],temporada=data['temporada'],descripcion=data['descripcion'],reseña=data['reseña'],youtube=data['youtube'])
            serie.save()

        return render(req,"formSerie.html")
    
    else:
        miFormulario=FormSerie()
        return render(req, "formSerie.html",{"miFormulario":miFormulario})