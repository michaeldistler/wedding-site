from django import forms
from rsvp.models import Rsvp


class RsvpForm(forms.ModelForm):
    class Meta:
        model = Rsvp
        fields = (
            "first_name",
            "last_name",
            "email",
            "number_of_guests",
        )
