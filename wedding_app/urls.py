from django.conf.urls import patterns, include, url
from django.conf import settings
from django.http import HttpResponse
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    url(r'^$', 'wedding_app.views.index', name='index'),
    url(r'^RSVP/', include('rsvp.urls', namespace="rsvp")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login, name="login"),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain")),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
