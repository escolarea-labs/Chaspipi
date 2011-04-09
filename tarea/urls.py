__author__ = 'fernando'

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('tarea.views',
    url(r'^crear/$', 'crear',
        name='crear_tarea'),

    url(r'^(?P<tarea_id>\d+)/hecha/$', 'cambiar_hecha',
        name='hecha_tarea'),
)
  