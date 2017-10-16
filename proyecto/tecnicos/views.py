from django.http import HttpResponse
from django.shortcuts import render
from .models import HorarioMes, HorarioDias, HorarioHoras, horariodias_horariomes, Tecnico
# Create your views here.

def ver_tecnicos(request):
	tecnicos = Tecnico.objects.all().order_by('primer_apellido')
	
	return render(request,'tecnicos/ver_tecnicos.html', { 'tecnicos':tecnicos })