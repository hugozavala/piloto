from django.conf.urls import patterns, include, url

from equipos import views

urlpatterns = patterns('', 
    # ex: /polls/
    #url(r'^$', views.ver_equipos, name='ver_equipos'),
    url(r'^equipos/$', views.ver_equipos, name='equipos-list'),
    
    url(r'^partes/$', views.ver_partes, name='partes-list'),
  
    url(r'^piezas/$', views.ver_piezas, name='piezas-list'),

    url(r'^estacion/$', views.EstacionListView.as_view(), name='estacion-list'),

  )