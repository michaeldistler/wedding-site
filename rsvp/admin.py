from django.contrib import admin
from rsvp.models import Rsvp


class RsvpAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'number_of_guests',
    )

admin.site.register(Rsvp, RsvpAdmin)
