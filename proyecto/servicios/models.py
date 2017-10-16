from django.db import models
from equipos.models import Equipo
from almacenes.models import PedidoAlmacen
from tecnicos.models import Tecnico

# Create your models here.
class Servicio(models.Model):

	tipo_de_mantenimiento = (
   	 ('Preventivo', 'Preventivo'),
   	 ('Correctivo', 'Correctivo'),
   	 ('Generales', 'Generales'),
	)

	codigo = models.CharField(max_length=30,unique='codigo')
	equipo = models.ForeignKey(Equipo)
	tecnico = models.ForeignKey(Tecnico)
	tareas = models.TextField(max_length=250)
	tipo_mantenimiento = models.CharField(max_length=30 ,choices=tipo_de_mantenimiento)
	pedido_almacen = models.ForeignKey(PedidoAlmacen)
	imagen_inicial = models.ImageField(upload_to="imagen_servicio/imagen_inicial")
	imagen_final = models.ImageField(upload_to="imagen_servicio/imagen_final")
	question_text = models.CharField(max_length=200)

	
	def __unicode__(self):
		return self.codigo


class HistorialConformidad(models.Model):
    servicio = models.ForeignKey(Servicio)
    choice_de_text = (
     ('Si', 'Si'),
   	 ('Puede mejorar', 'Puede mejorar'),
   	 ('No', 'No'),
	)
    choice_text = models.CharField(max_length=20,choices=choice_de_text)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
    	return self.choice_text


class Cronograma(models.Model):
	codigo = (
   	 ('ENERO 2016', 'ENERO 2016'),
   	 ('FEBRERO 2016', 'FEBRERO 2016'),
   	 ('MARZO 2016', 'MARZO 2016'),
   	 ('ABRIL 2016', 'ABRIL 2016'),
   	 ('MAYO 2016', 'MAYO 2016'),
   	 ('JUNIO 2016', 'JUNIO 2016'),
   	 ('JULIO 2016', 'JULIO 2016'),
   	 ('AGOSTO 2016', 'AGOSTO 2016'),
   	 ('SEPTIEMBRE 2016', 'SEPTIEMBRE 2016'),
   	 ('OCTUBRE 2016', 'OCTUBRE 2016'),
   	 ('NOVIEMBRE 2016', 'NOVIEMBRE 2016'),
   	 ('DICIEMBRE 2016', 'DICIEMBRE 2016'),
	)
	codigo = models.CharField(max_length=30, choices=codigo, unique='codigo')
	servicio=models.ManyToManyField(Servicio, through='servicio_cronograma')
	

	def __unicode__(self):
		return self.codigo


class servicio_cronograma(models.Model):
	cronograma=models.ForeignKey(Cronograma)
	servicio=models.ForeignKey(Servicio)
	fecha_inicio = models.DateTimeField()
	fecha_termino = models.DateTimeField()
	def __unicode__(self):
		return self.cronograma.codigo
