from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.urls import reverse_lazy
from .models import *
from .forms import *
# Create your views here.

class Home(View):

    def get(self, request):
        return render(request, 'base/home.html')
    
class About(View):

    def get(self, request):
        return render(request, 'blog/About.html')

class ArticuloListView(ListView):
    model = Articulos
    template_name = 'blog/articulos/articulo_list.html'
    

class ArticuloDetailView(DetailView):
    model = Articulos
    template_name = 'blog/articulos/articulo_detail.html'

class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulos
    form_class = ArticuloForm
    login_url = 'Iniciar_Sesion'
    template_name = 'blog/articulos/articulo_form.html'
    success_url = reverse_lazy('Listado')

    def form_valid(self, form):
        form.instance.Autor = self.request.user
        return super().form_valid(form)

class ArticuloUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articulos
    form_class = ArticuloForm
    template_name = 'blog/articulos/articulo_form.html'
    success_url = reverse_lazy('Listado')

    def test_func(self):
        usuario_actual = self.request.user
        return usuario_actual == self.get_object().Autor or usuario_actual.is_superuser

class ArticuloDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articulos
    template_name = 'blog/articulos/articulo_confirm_delete.html'
    success_url = reverse_lazy('Listado')

    def test_func(self):
        usuario_actual = self.request.user
        return usuario_actual == self.get_object().Autor or usuario_actual.is_superuser

