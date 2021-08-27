from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name='index.html'

    
class EstudiantesView(TemplateView):
    template_name='estudiantes.html'

class AdministadoresView(TemplateView):
    template_name='administradores.html'
    
class InicioView(TemplateView):
    template_name='inicio.html'

    
