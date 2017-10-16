from django.contrib import admin
from .models import  Estacion, Pieza, Parte, HistorialEquipo, Equipo

# Register your models here.
class HistorialEquipoInline(admin.TabularInline):
    model = HistorialEquipo
    extra = 3
    

class EquipoAdmin(admin.ModelAdmin):
	list_display = ('rotulo', 'nombre', 'tipo_equipo','marca','modelo','numero_serie','partes')
	search_fields = ['nombre']
	inlines = [HistorialEquipoInline]

admin.site.register(Equipo, EquipoAdmin)
admin.site.register(HistorialEquipo)

@admin.register(Estacion)

class EstacionAdmin(admin.ModelAdmin):
	list_display = ('codigo','nombre','caracteristicas','equipo')
	search_fields = ['codigo']

@admin.register(Pieza)

class PiezaAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'datos')
	list_filter = ['codigo']

@admin.register(Parte)

class ParteAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'caracteristicas','pieza')
	list_filter = ['nombre']