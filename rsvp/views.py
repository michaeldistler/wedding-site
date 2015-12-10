from django.shortcuts import render
from django.http import JsonResponse

from rsvp.forms import RsvpForm
from rsvp.models import Rsvp


# Needs work
def rsvp_form(request):
    if request.method == "POST":
        rsvp_form = RsvpForm(request.POST)
        if rsvp_form.is_valid():
            rsvp, created = Rsvp.objects.get_or_create(
                first_name=rsvp_form.cleaned_data['first_name'],
                last_name=rsvp_form.cleaned_data['last_name'],
                email=rsvp_form.cleaned_data['email'],
                number_of_guests=rsvp_form.cleaned_data['number_of_guests'],
            )

            return render(request, 'index.html', {})
        else:
            return JsonResponse({'error': 'Error, Will Robinson.'})
    else:
        user = request.user
        rsvp_form = RsvpForm()

    return render(request, 'rsvp/rsvp.html', {
        "rsvp_form": rsvp_form,
        "user": user,
    })
