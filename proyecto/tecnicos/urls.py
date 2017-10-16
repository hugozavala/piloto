from django.conf.urls import patterns, include, url

from tecnicos import views

urlpatterns = patterns('', 
    # ex: /polls/
    #url(r'^$', views.ver_equipos, name='ver_equipos'),
    url(r'^tecnicos/$', views.ver_tecnicos, name='tecnicos-list'),
    
    

  )