from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Tecnico(models.Model):


	DNI = models.PositiveIntegerField(unique='DNI')
	primer_nombre = models.CharField(max_length=30)
	segundo_nombre = models.CharField(max_length=35,null=True, blank=True)
	primer_apellido = models.CharField(max_length=35)
	segundo_apellido = models.CharField(max_length=35,null=True, blank=True)
	edad = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(90)])
	distrito = models.CharField(max_length=30)
	avenida = models.CharField(max_length=30,null=True, blank=True)
	calle = models.CharField(max_length=30,null=True, blank=True)
	urbanizacion = models.CharField(max_length=30,null=True, blank=True)
	manzana = models.CharField(max_length=30,null=True, blank=True)
	jiron = models.CharField(max_length=30,null=True, blank=True)
	lote = models.CharField(max_length=4,null=True, blank=True)
	numero_vivienda = models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(9999)])
	imagen_tecnico = models.ImageField(upload_to="imagen_tecnico")


	def __unicode__(self):
		return self.primer_apellido

class HorarioHoras(models.Model):

	horario = (
   	 ('06:00:00AM a 14:00:00PM', '06:00:00AM a 14:00:00PM'),
   	 ('14:00:00PM a 22:00:00PM', '14:00:00PM a 22:00:00PM'),
   	 ('22:00:00PM a 06:00:00AM', '22:00:00PM a 06:00:00AM'),
	)
	horario = models.CharField(max_length=30, choices=horario)
	numero_horas = models.IntegerField()
	tecnico = models.ForeignKey(Tecnico)


	def __unicode__(self):
		return self.horario

class HorarioDias(models.Model):

	codigo = models.CharField(max_length=25, unique='codigo')
	numero_horas = models.IntegerField()
	horariohoras = models.ForeignKey(HorarioHoras)

	def __unicode__(self):
		return self.codigo

class HorarioMes(models.Model):

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
	numero_dias = models.IntegerField()
	horariodias = models.ManyToManyField(HorarioDias, through='horariodias_horariomes')

	def __unicode__(self):
		return self.codigo

class horariodias_horariomes(models.Model):
	horariomes = models.ForeignKey(HorarioMes)
	horariodias = models.ForeignKey(HorarioDias)

	def __unicode__(self):
		return self.horariomes.codigo