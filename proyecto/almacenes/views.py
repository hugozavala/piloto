from django.http import HttpResponse
from django.shortcuts import render
from .models import Instrumento, Herramienta, Accesorio, Indumentaria, PedidoAlmacen, HistorialPedidoAlmacen, Almacen
# Create your views here.

def ver_herramientas(request):
	herramientas = Herramienta.objects.all().order_by('nombre')
	
	return render(request,'almacenes/ver_herramientas.html', { 'herramientas':herramientas })

def ver_accesorios(request):
	accesorios = Accesorio.objects.all().order_by('nombre')
	
	return render(request,'almacenes/ver_accesorios.html', { 'accesorios':accesorios })

def ver_indumentarias(request):
	indumentarias = Indumentaria.objects.all().order_by('nombre')
	
	return render(request,'almacenes/ver_indumentarias.html', { 'indumentarias':indumentarias })

def ver_instrumentos(request):
	instrumentos = Instrumento.objects.all().order_by('nombre')
	
	return render(request,'almacenes/ver_instrumentos.html', { 'instrumentos':instrumentos })

def ver_pedidosalmacen(request):
	pedidosalmacen = PedidoAlmacen.objects.all().order_by('nombre')
	
	return render(request,'almacenes/ver_pedidosalmacen.html', { 'pedidosalmacen':pedidosalmacen })

def ver_almacenes(request):
	almacenes = Almacen.objects.all().order_by('nombre')
	
	return render(request,'almacenes/ver_almacenes.html', { 'almacenes':almacenes })
