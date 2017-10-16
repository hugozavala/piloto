from django.contrib import admin
from .models import HistorialConformidad, Servicio, Cronograma, servicio_cronograma

# Register your models here.
class HistorialConformidadInline(admin.TabularInline):
    model = HistorialConformidad
    extra = 3


class ServicioAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'equipo', 'tecnico', 'tareas', 'tipo_mantenimiento', 'pedido_almacen')
	search_fields = ['codigo']
	inlines = [HistorialConformidadInline]
	

admin.site.register(Servicio, ServicioAdmin)
admin.site.register(HistorialConformidad)

class servicio_cronogramaInline(admin.TabularInline):
    model = servicio_cronograma


class cronogramaAdmin(admin.ModelAdmin):
    inlines = (servicio_cronogramaInline,)
    search_fields = ['codigo']

admin.site.register(Cronograma, cronogramaAdmin)