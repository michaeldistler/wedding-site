from django.shortcuts import render
from rsvp.forms import RsvpForm


def index(request):
    rsvp_form = RsvpForm()
    return render(request, 'index.html', {
        "rsvp_form": rsvp_form,
    })
