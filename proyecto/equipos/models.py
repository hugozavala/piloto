from django.db import models


# Create your models here.

class Pieza(models.Model):

	codigo = models.CharField(max_length=20,unique='codigo')
	datos = models.TextField(max_length=400,null=True, blank=True)
	imagen_pieza = models.ImageField(upload_to="imagen_pieza")
	
	def __unicode__(self):
		return self.codigo



class Parte(models.Model):

	nombre = models.CharField(max_length=30,unique='nombre')
	caracteristicas = models.TextField(max_length=850,null=True, blank=True)
	imagen_parte = models.ImageField(upload_to="imagen_parte")
	pieza = models.ForeignKey(Pieza)

	def __unicode__(self):
		return self.nombre

class Equipo(models.Model):


	rotulo = models.CharField(max_length=10,unique='rotulo')
	nombre = models.CharField(max_length=40)
	tipo_de_equipo = (
   	 ('AA', 'AA'),
   	 ('EE', 'EE'),
   	 ('V', 'V'),
	)
	tipo_equipo = models.CharField(max_length=10 ,choices=tipo_de_equipo)
	marca = models.CharField(max_length=20,null=True, blank=True)
	modelo = models.CharField(max_length=20,null=True, blank=True)
	numero_serie = models.CharField(max_length=30,null=True, blank=True)
	imagen_equipo = models.ImageField(upload_to="imagen_equipo")
	partes = models.ForeignKey(Parte)
	mantenimientos_realizados = models.CharField(max_length=200)



	def __unicode__(self):
		return self.nombre

class Estacion(models.Model):

	codigo = models.CharField(max_length=15,unique='codigo')
	nombre = models.CharField(max_length=40)
	caracteristicas = models.TextField(max_length=200, null=True, blank=True)
	imagen_estacion = models.ImageField(upload_to="imagen_estacion")
	equipo = models.ForeignKey(Equipo)

	def __unicode__(self):
		return self.codigo





class HistorialEquipo(models.Model):
    question = models.ForeignKey(Equipo)
    fecha_mantenimiento = models.CharField(max_length=200)
    
    def __unicode__(self):
    	
	return self.fecha_mantenimiento



