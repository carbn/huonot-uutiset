from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^tilastot/(?P<year>[0-9]{4})/(?P<week>[0-9]{2})/$', views.home, name='weekly_stats'),
    url(r'^sivusto/(?P<id>[0-9]+)/$', views.site, name='site'),
    url(r'^tietoa$', views.home, name='about'),
]
