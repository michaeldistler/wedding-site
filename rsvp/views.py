from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse

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


def send_email(request, to_email):
    subject = ''
    message = ''
    from_email = 'agorriewedding@gmail.com'
    to_email = to_email
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, [to_email])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/RSVP/')
    else:
        return HttpResponse('Make sure all fields are valid.')
