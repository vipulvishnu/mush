from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/v1/', include('applications.api.urls')),
                       url(r'^', include('applications.web.urls')),
                       )
