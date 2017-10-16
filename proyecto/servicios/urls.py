from django.conf.urls import patterns, include, url

from servicios import views

urlpatterns = patterns('', 
    # ex: /polls/
    #url(r'^$', views.ver_equipos, name='ver_equipos'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^servicios/$', views.ver_servicios, name='servicios-list'),

  )