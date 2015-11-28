from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'rsvp.views.rsvp_form', name='rsvp_form'),
)
