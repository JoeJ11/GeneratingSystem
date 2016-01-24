from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^([0-9]+)/message/$', views.message, name='message'),
    url(r'^([0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^([0-9]+)/response/$', views.response, name='response'),
]
