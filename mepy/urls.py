from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cv$', views.circullumVitae, name='cv'),
    url(r'^about$', views.aboutMe, name='about')
]
