from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'proyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^equipos/', include('equipos.urls', namespace="equipos")),

	url(r'^almacenes/', include('almacenes.urls', namespace="almacenes")),

    url(r'^tecnicos/', include('tecnicos.urls', namespace="tecnicos")),

    url(r'^servicios/', include('servicios.urls', namespace="servicios")),

    url(r'^admin/', include(admin.site.urls)),
]

from django.conf import settings
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))