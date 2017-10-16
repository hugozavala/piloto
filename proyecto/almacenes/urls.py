from django.conf.urls import patterns, include, url

from almacenes import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^herramientas/$', views.ver_herramientas, name='herramientas-list'),
    
    url(r'^accesorios/$', views.ver_accesorios, name='accesorios-list'),

    url(r'^indumentarias/$', views.ver_indumentarias, name='indumentarias-list'),
  
  	url(r'^instrumentos/$', views.ver_instrumentos, name='instrumentos-list'),

  	url(r'^pedidosalmacen/$', views.ver_pedidosalmacen, name='pedidosalmacen-list'),

  	url(r'^almacenes/$', views.ver_almacenes, name='almacenes-list'),
)