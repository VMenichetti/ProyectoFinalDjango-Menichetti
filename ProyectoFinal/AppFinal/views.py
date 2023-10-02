from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import *
from .forms import FormPelicula

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