from django.contrib import admin
from rsvp.models import Rsvp


class RsvpAdmin(admin.ModelAdmin):
    list_display = (
        'user',
    )

admin.site.register(Rsvp, RsvpAdmin)
