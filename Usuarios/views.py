from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from .models import *
from .forms import *

from django.contrib.auth.mixins import LoginRequiredMixin



from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

#Usuarios

class Creacion_Usuario( CreateView ):

    model = User
    form_class = Usuario_Form
    template_name = 'usuarios/crear.html'
    success_url = reverse_lazy('Home')

class Editar_Usuario( LoginRequiredMixin , UpdateView ):

    model = User
    form_class = Usuario_Form_2
    template_name = 'usuarios/editar.html'
    success_url = reverse_lazy('Home')

    