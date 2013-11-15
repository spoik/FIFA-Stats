from django.conf.urls import patterns, url

from .views import MatchCreateView

urlpatterns = patterns('',
    url(r'^$', MatchCreateView.as_view(), name='list'),
    url(r'^create/$', MatchCreateView.as_view(), name='create'),
)
