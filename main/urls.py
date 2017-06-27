from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_occupations, name='list_occupations'),
    url(r'^occupation/(?P<pk>\d+)/$', views.occupation_detail, name='occupation_detail'),
    url(r'^occupation/(?P<pk>\d+)/occupation_page$', views.occupation_page, name='occupation_page'),
]