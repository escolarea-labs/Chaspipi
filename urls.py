from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'intro_django.views.home', name='home'),
    # url(r'^intro_django/', include('intro_django.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'lista.views.crear',
        name='home'),

    url(r'^(?P<codigo>[a-zA-Z0-9]+)/$', 'lista.views.mostrar',
        name='lista'),

    url(r'^tarea/', include('tarea.urls')),
)


urlpatterns += staticfiles_urlpatterns()