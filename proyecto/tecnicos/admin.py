from django.contrib import admin
from .models import Tecnico, HorarioHoras, HorarioDias, HorarioMes, horariodias_horariomes

# Register your models here.

@admin.register(Tecnico)

class TecnicoAdmin(admin.ModelAdmin):
	list_display = ('DNI','primer_nombre','segundo_nombre', 'primer_apellido','segundo_apellido','edad','distrito','avenida','calle','urbanizacion','manzana','jiron','lote','numero_vivienda')
	search_fields = ['primer_apellido']

@admin.register(HorarioHoras)

class HorarioHorasAdmin(admin.ModelAdmin):
	list_display = ('horario','numero_horas','tecnico')
	search_fields = ['horario']


class HorarioDiasAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'numero_horas', 'horariohoras')
	search_fields = ['codigo']
	
admin.site.register(HorarioDias, HorarioDiasAdmin)


class horariodias_horariomesInline(admin.TabularInline):
    model = horariodias_horariomes


class HorarioMesAdmin(admin.ModelAdmin):
    inlines = (horariodias_horariomesInline,)
    search_fields = ['codigo']

admin.site.register(HorarioMes, HorarioMesAdmin)