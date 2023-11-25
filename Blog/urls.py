from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("" , Home.as_view() , name = "Home" ) ,
    path("about/" , About.as_view() , name = "About") ,
    
    path('articulo/nuevo/', ArticuloCreateView.as_view(), name='Crear'),
    path('articulo/listar/', ArticuloListView.as_view(), name='Listado'),
    path('articulo/<int:pk>/', ArticuloDetailView.as_view(), name='Detalles'),
    path('articulo/<int:pk>/editar/', ArticuloUpdateView.as_view(), name='Editar'),
    path('articulo/<int:pk>/eliminar/', ArticuloDeleteView.as_view(), name='Borrar'),
]