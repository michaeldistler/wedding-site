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
        widgets = {
            'first_name': forms.TextInput(attrs={
                'name': 'first_name',
                'type': 'text',
                'placeholder': 'First Name',
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'name': 'last_name',
                'type': 'text',
                'placeholder': 'Last Name',
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'name': 'email',
                'type': 'text',
                'placeholder': 'Email',
                'class': 'form-control',
            }),
            'number_of_guests': forms.NumberInput(attrs={
                'name': 'number_of_guests',
                'type': 'text',
                'placeholder': 'Numero Of Guests',
                'class': 'form-control',
            }),
        }
