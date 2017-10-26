from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.circullumVitae, name='cv'),
    url(r'^$', views.aboutMe, name='about')
]
