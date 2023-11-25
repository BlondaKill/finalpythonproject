from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Articulos(models.Model):
    Titulo = models.CharField( max_length = 150 )
    Subtitulo = models.CharField( max_length = 150 )
    Contenido = models.TextField( max_length = 2000 )
    Imagen = models.ImageField( upload_to = 'Articulos/' , blank=True , null=True)
    Fecha = models.DateTimeField( auto_now = True )
    Autor = models.ForeignKey(User, on_delete=models.CASCADE)
