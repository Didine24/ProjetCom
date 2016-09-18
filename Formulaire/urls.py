from django.conf.urls import url
from . import views

urlpatterns = [
    # /form/
    url(r'^$', views.accueil, name = 'accueil'),
    url(r'^index', views.index, name = 'index'),
    # /form/id
    
    url(r'^(?P<form_id>[0-9]+)/$', views.detail, name = 'detail'),
    url(r'^create', views.create, name = 'create'),
]
