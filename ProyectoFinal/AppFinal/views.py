from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import *
from .forms import FormPelicula,FormSerie
from django import forms




def lista_peliculas(req):
    peliculas = Pelicula.objects.all()
    return render(req, "lista_peliculas.html", {"lista_peliculas": peliculas})


def lista_series(req):
    series = Serie.objects.all()
    return render(req, "lista_series.html", {"lista_series": series})


def inicio(req):
    return render(req, "inicio.html")

def peliculas(req, start=0):
    cant_por_pagina = 8

    if req.GET.get('direction') == 'next':
        start += 1
    elif req.GET.get('direction') == 'previous':
        start -= 1

    inicio = int(start)*cant_por_pagina
    final = (int(start) + 1)*cant_por_pagina
    lista_peliculas = Pelicula.objects.all()[inicio:final]

    return render(req, "peliculas.html", {"lista_peliculas": lista_peliculas, "current_page": start})


def series(req, start=0):
    cant_por_pagina = 8

    if req.GET.get('direction') == 'next':
        start += 1
    elif req.GET.get('direction') == 'previous':
        start -= 1

    inicio = int(start)*cant_por_pagina
    final = (int(start) + 1)*cant_por_pagina
    lista_series = Serie.objects.all()[inicio:final]

    return render(req, "series.html", {"lista_series": lista_series, "current_page": start})

def usuarios(req):
    return render(req, "inicio.html")

def error(req):
    return render(req, "error404.html")


# CRUD PELICULAS

# Funcion Crear Pelicula

def crear_pelicula(request):
    if request.method == 'POST':
        form = FormPelicula(request.POST, request.FILES)
        if form.is_valid():
            data=form.cleaned_data
            pelicula=Pelicula(
                nombre=data['nombre'],
                subtitulo=data['subtitulo'],
                imagenpelicula=data['imagen'],
                descripcion=data['descripcion'],
                reseña=data['reseña'],
                youtube=data['youtube'])
            pelicula.save()

            return render(request,"formPelicula.html")
    else:
        form = PeliculaForm()
    return render(request, 'formPelicula.html', {'form': form})

# Funcion Eliminar Pelicula

def eliminar_pelicula(req, id):

    if req.method == 'POST':

        pelicula = Pelicula.objects.get(id=id)
        pelicula.delete()

        pelicula = Pelicula.objects.all()

        return render(req, "lista_peliculas.html", {"peliculas": peliculas})

# Funcion Editar Pelicula
    
def editar_pelicula(req, id):
        
    pelicula = Pelicula.objects.get(id=id)

    if req.method == 'POST':

        miFormulario = FormPelicula(req.POST, req.FILES)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            pelicula.nombre=data["nombre"]
            pelicula.subtitulo=data["subtitulo"]
            pelicula.imagenpelicula=data["imagen"]
            pelicula.descripcion=data["descripcion"]
            pelicula.reseña=data["reseña"]
            pelicula.youtube=data["youtube"]
            pelicula.save()

            return render(req, "inicio.html")
    else:

        miFormulario = FormPelicula(initial={
            "nombre": pelicula.nombre,
            "subtitulo": pelicula.subtitulo,
            "imagen": pelicula.imagenpelicula,
            "descripcion": pelicula.descripcion,
            "reseña": pelicula.reseña,
            "youtube": pelicula.youtube,
        })
        return render(req, "editarPelicula.html", {"miFormulario": miFormulario, "id": pelicula.id})

# CRUD SERIES

# Funcion Crear Serie

def crear_serie(request):
    if request.method == 'POST':
        form = FormSerie(request.POST, request.FILES)
        if form.is_valid():
            data=form.cleaned_data
            serie=Serie(
                nombre=data['nombre'],
                subtitulo=data['subtitulo'],
                imagenserie=data['imagen'],
                temporada=data ['temporada'],
                descripcion=data['descripcion'],
                reseña=data['reseña'],
                youtube=data['youtube'])
            serie.save()

            return render(request,"formSerie.html")
    else:
        form = FormSerie()
    return render(request, 'formSerie.html', {'form': form})

# Funcion Eliminar Serie

def eliminar_serie(req, id):

    if req.method == 'POST':

        serie = Serie.objects.get(id=id)
        serie.delete()

        serie = Serie.objects.all()

        return render(req, "lista_series.html", {"series": series})

# Funcion Editar Serie
    
def editar_serie(req, id):
        
    serie = Serie.objects.get(id=id)

    if req.method == 'POST':

        miFormulario = FormSerie(req.POST, req.FILES)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            serie.nombre=data["nombre"]
            serie.subtitulo=data["subtitulo"]
            serie.imagenserie=data["imagen"]
            serie.temporada=data["temporada"]
            serie.descripcion=data["descripcion"]
            serie.reseña=data["reseña"]
            serie.youtube=data["youtube"]
            serie.save()

            return render(req, "inicio.html")
    else:

        miFormulario = FormSerie(initial={
            "nombre": serie.nombre,
            "subtitulo": serie.subtitulo,
            "imagen": serie.imagenserie,
            "temporada": serie.temporada,
            "descripcion": serie.descripcion,
            "reseña": serie.reseña,
            "youtube": serie.youtube,
        })
        return render(req, "editarSerie.html", {"miFormulario": miFormulario, "id": serie.id})

    

# BUSQUEDA

def busquedaPelicula(req):
    return render(req,"busquedaPelicula.html")

def buscar(req:HttpRequest):
    if req.GET["nombre"]:
        nombre=req.GET["nombre"]
        nombres=Pelicula.objects.filter(nombre__icontains=nombre)
        return render(req, "resultadoBusqueda.html",{"nombres":nombres})
    
    else:
        return HttpResponse(f'Debe agregar una pelicula')
    
class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['nombre', 'subtitulo', 'imagenpelicula', 'descripcion', 'reseña', 'youtube']


