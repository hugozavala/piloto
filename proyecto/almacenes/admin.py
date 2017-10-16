from django.contrib import admin
from .models import  Herramienta, Instrumento, Accesorio, Indumentaria, PedidoAlmacen, HistorialPedidoAlmacen, Almacen

# Register your models here.

@admin.register(Instrumento)

class InstrumentoAdmin(admin.ModelAdmin):
	list_display = ('codigo','nombre','marca')
	list_filter = ['nombre']


@admin.register(Herramienta)

class HerramientaAdmin(admin.ModelAdmin):
	list_display = ('codigo','nombre','marca')
	list_filter = ['nombre']

@admin.register(Accesorio)

class AccesorioAdmin(admin.ModelAdmin):
	list_display = ('codigo','nombre','marca', 'modelo', 'fecha_vencimiento')
	list_filter = ['nombre']

@admin.register(Indumentaria)

class IndumentariaAdmin(admin.ModelAdmin):
	list_display = ('codigo','nombre','talla')
	list_filter = ['nombre']

class HistorialPedidoAlmacenInline(admin.TabularInline):
    model = HistorialPedidoAlmacen
    extra = 4

class PedidoAlmacenAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'nombre','fecha_pedido','herramienta','accesorio','indumentaria')
	search_fields = ['codigo']
	inlines = [HistorialPedidoAlmacenInline]

admin.site.register(PedidoAlmacen, PedidoAlmacenAdmin)
admin.site.register(HistorialPedidoAlmacen)

class AlmacenAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'nombre')
	search_fields = ['codigo']

admin.site.register(Almacen, AlmacenAdmin)