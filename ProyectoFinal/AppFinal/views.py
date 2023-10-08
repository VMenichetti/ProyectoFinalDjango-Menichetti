from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import *
from .forms import FormPelicula,FormSerie
from django import forms




def lista_peliculas(req):
    peliculas = Pelicula.objects.all()
    return render(req, "lista_peliculas.html", {"lista_peliculas": peliculas})

def inicio(req):
    return render(req, "inicio.html")

def peliculas(req, start=0):
    cant_por_pagina = 3

    if req.GET.get('direction') == 'next':
        start += 1
    elif req.GET.get('direction') == 'previous':
        start -= 1

    inicio = int(start)*cant_por_pagina
    final = (int(start) + 1)*cant_por_pagina
    lista_peliculas = Pelicula.objects.all()[inicio:final]

    return render(req, "peliculas.html", {"lista_peliculas": lista_peliculas, "current_page": start})



def series(req):
    return render(req, "inicio.html")

def usuarios(req):
    return render(req, "inicio.html")

def error(req):
    return render(req, "error404.html")


# CRUD PELICULAS

# Funcion Registro/Creacion

# def formPelicula(req):
    # print('method',req.method)
    # print('POST',req.POST)

    # if req.method == 'POST':
    #     miFormulario=FormPelicula(req.POST)
    #     if miFormulario.is_valid():
    #         data=miFormulario.cleaned_data
    #         pelicula=Pelicula(
    #             nombre=data['nombre'],
    #             subtitulo=data['subtitulo'],
    #             imagenpelicula=data['imagen'],
    #             descripcion=data['descripcion'],
    #             reseña=data['reseña'],
    #             youtube=data['youtube'])
    #         pelicula.save()

    #     return render(req,"formPelicula.html")
    
    # else:
    #     miFormulario=FormPelicula()
    #     return render(req, "formPelicula.html",{"miFormulario":miFormulario})

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
            return redirect('lista_peliculas') 
    else:
        form = PeliculaForm()
    return render(request, 'formPelicula.html', {'form': form})

# Funcion Eliminar Pelicula

def eliminar_pelicula(req, id):

    if req.method == 'POST':

        pelicula = Pelicula.objects.get(id=id)
        pelicula.delete()

        pelicula = Pelicula.objects.all()

        return redirect('lista_peliculas')

# Funcion Editar Pelicula
    
# Función Editar
    
def editar_pelicula(req, id):
        
    pelicula = Pelicula.objects.get(id=id)

    if req.method == 'POST':

        miFormulario = FormPelicula(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            pelicula.nombre=data["nombre"],
            pelicula.subtitulo=data["subtitulo"],
            pelicula.imagenpelicula=data["imagen"],
            pelicula.descripcion=data["descripcion"],
            pelicula.reseña=data["reseña"],
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


def formSerie(req):
    print('method',req.method)
    print('POST',req.POST)

    if req.method == 'POST':
        miFormulario=FormSerie(req.POST)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            serie=Serie(
                nombre=data['nombre'],
                subtitulo=data['subtitulo'],
                imagen=data['imagen'],
                temporada=data['temporada'],
                descripcion=data['descripcion'],
                reseña=data['reseña'],
                youtube=data['youtube'])
            serie.save()

        return render(req,"formSerie.html")
    
    else:
        miFormulario=FormSerie()
        return render(req, "formSerie.html",{"miFormulario":miFormulario})
    

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


