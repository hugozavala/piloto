from django.http import HttpResponse
from django.shortcuts import render
from .models import Equipo, Estacion, Pieza, Parte, HistorialEquipo
from django.views.generic import ListView

# Create your views here.

def ver_equipos(request):
	equipos = Equipo.objects.all().order_by('nombre')
	
	return render(request,'equipos/ver_equipos.html', { 'equipos':equipos })

def ver_partes(request):
	partes = Parte.objects.all().order_by('nombre')
	return render(request,'equipos/ver_partes.html', { 'partes':partes })

def ver_piezas(request):
	piezas = Pieza.objects.all().order_by('codigo')
	return render(request,'equipos/ver_piezas.html', { 'piezas':piezas })

class EstacionListView(ListView):
    model = Estacion

