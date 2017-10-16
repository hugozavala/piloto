from django.db import models


# Create your models here.

class Instrumento(models.Model):

	codigo = models.CharField(max_length=15,unique='codigo')
	nombre = models.CharField(max_length=40)
	marca = models.CharField(max_length=30, null=True, blank=True)
	imagen_instrumento = models.ImageField(upload_to='imagen_instrumento')

	def __unicode__(self):
		return self.nombre



class Herramienta(models.Model):


	codigo = models.CharField(max_length=10,unique='codigo')
	nombre = models.CharField(max_length=30)
	marca = models.CharField(max_length=30,null=True, blank=True)
	imagen_herramienta = models.ImageField(upload_to='imagen_herramienta')
	

	def __unicode__(self):
	   	return self.nombre



class Accesorio(models.Model):
	codigo = models.CharField(max_length=10,unique='codigo')
	nombre = models.CharField(max_length=30)
	marca = models.CharField(max_length=30,null=True, blank=True)
	modelo = models.CharField(max_length=25,null=True, blank=True)
	fecha_vencimiento = models.DateField(null=True, blank=True)
	imagen_accesorio = models.ImageField(upload_to='imagen_accesorio',null=True, blank=True)


	def __unicode__(self):
	   	return self.nombre



class Indumentaria(models.Model):


	codigo = models.CharField(max_length=15,unique='codigo')
	nombre = models.CharField(max_length=30)
	talla = models.CharField(max_length=30)
	imagen_indumentaria = models.ImageField(upload_to='imagen_indumentaria')


	def __unicode__(self):
	   	return self.nombre



class PedidoAlmacen(models.Model):
	codigo = models.CharField(max_length=30, unique=True)
	nombre = models.CharField(max_length=45)
	fecha_pedido = models.DateTimeField()
	instrumento = models.ForeignKey(Instrumento)
	herramienta = models.ForeignKey(Herramienta)
	accesorio = models.ForeignKey(Accesorio)
	indumentaria = models.ForeignKey(Indumentaria)

	def __unicode__(self):
	   	return self.nombre


class HistorialPedidoAlmacen(models.Model):
    pedido_almacen = models.ForeignKey(PedidoAlmacen)
    choice_de_text = (
     ('P/INDM', 'P/INDM'),
   	 ('P/HRM', 'P/HRM'),
   	 ('P/ACC', 'P/ACC'),
   	 ('P/INSTM','P/INSTM')
	)
    choice_text = models.CharField(max_length=20,choices=choice_de_text)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
    	return self.choice_text

class Almacen(models.Model):
	codigo = models.CharField(max_length=30, unique=True)
	nombre = models.CharField(max_length=45)
	pedido_almacen = models.ForeignKey(PedidoAlmacen)
	

	def __unicode__(self):
	   	return self.nombre