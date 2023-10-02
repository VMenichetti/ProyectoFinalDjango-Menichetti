from django import forms

class FormPelicula(forms.Form):
    nombre = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=40)
    imagen = forms.ImageField(required=False)
    descripcion = forms.CharField(max_length=150)
    reseña = forms.CharField(max_length=150)
    youtube = forms.URLField()