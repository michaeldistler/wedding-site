from django.shortcuts import render
from django.http import HttpResponse

from rsvp.forms import RsvpForm

# Needs work
def rsvp_form(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            rsvp_form = RsvpForm(request.POST)
            if rsvp_form.is_valid():
                rsvp_form.user = request.user
                rsvp_form.save()
                return render(request, 'index.html', {})
            else:
                return HttpResponse("rsvp was not sent.")
        else:
            user = request.user
            rsvp_form = RsvpForm()

    return render(request, 'rsvp/rsvp.html', {
        "rsvp_form": rsvp_form,
        "user": user,
    })
