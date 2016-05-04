from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^zipcode/$', views.zipcode, name='zipcode'),
    url(r'^fillzipcode/$', views.fillz, name = 'fillz'),
    url(r'^f/(?P<zid>[0-9]+)$', views.mform, name = 'mform'),
    # url(r'^f/$', views.mform, name = 'mform'),
    url(r'^p/$', views.prob, name = 'prob'),
]
