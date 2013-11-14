from django.conf.urls import patterns, url

from .views import MatchFormView

urlpatterns = patterns('',
    url(r'^$', MatchFormView.as_view(), name='list'),
    url(r'^create/$', MatchFormView.as_view(), name='create'),
)
