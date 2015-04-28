from django.conf.urls import patterns, include, url
from django.conf import settings
import Plato.views as platoV


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TheMatrix.views.home', name='home'),
    # url(r'^TheMatrix/', include('TheMatrix.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Plato.views.home', name='home'),
    url(r'^anchoring/', 'Plato.views.anchoring', name='anchoring'),
    url(r'^perception/', 'Plato.views.perception', name='perception'),
    url(r'^richer/', 'Plato.views.richer', name='richer'),

#    url(r'^$', platoV.PostListView, name='list'),
    url(r'^post/', include('Plato.urls'))
)
