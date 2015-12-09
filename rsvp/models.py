from django.db import models


class Rsvp(models.Model):
    first_name = models.CharField(null=True, max_length=100)
    last_name = models.CharField(null=True, max_length=100)
    email = models.EmailField(null=True)
    number_of_guests = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return '{}'.format(self.last_name, self.first_name, self.email)
