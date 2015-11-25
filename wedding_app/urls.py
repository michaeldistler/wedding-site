from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'wedding_app.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
