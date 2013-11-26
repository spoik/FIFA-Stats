from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('main.urls', namespace='main')),
    url(r'^matches/', include('matches.urls', namespace='matches')),
    url(r'^admin/', include(admin.site.urls)),
)
