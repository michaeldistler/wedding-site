from django.conf.urls import patterns, include, url
from django.http import HttpResponse
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'wedding_app.views.index', name='index'),

    url(r'^RSVP/$', include('rsvp.urls', namespace="rsvp")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain")),
)
