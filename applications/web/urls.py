from django.conf.urls import patterns, include, url

from applications.web import views

urlpatterns = patterns('',
                       url(r'^$', views.HomeView.as_view(), name='home'),
                       )
