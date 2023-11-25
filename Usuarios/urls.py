from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path( "Crear/" , Creacion_Usuario.as_view() , name = 'Crear_Usuario' ) ,
    path( "Iniciar/" , LoginView.as_view( template_name = 'usuarios/login.html' ) , name = 'Iniciar_Sesion' ) ,
    path( "Cerrar/" , LogoutView.as_view() , name='Cerrar_Sesion') ,
    path( "Editar/<int:pk>" , Editar_Usuario.as_view() , name = 'Editar_Usuario' ) ,
    
]