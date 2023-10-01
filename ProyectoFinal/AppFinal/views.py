from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def inicio(req):
    return render(req, "inicio.html")

def peliculas(req):
    return render(req, "peliculas.html")

def series(req):
    return render(req, "inicio.html")

def usuarios(req):
    return render(req, "inicio.html")