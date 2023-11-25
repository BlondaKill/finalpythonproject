from django import forms
from .models import Articulos

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = ['Titulo', 'Subtitulo', 'Contenido', 'Imagen']