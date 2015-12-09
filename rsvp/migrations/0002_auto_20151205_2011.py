# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rsvp',
            name='user',
        ),
        migrations.AddField(
            model_name='rsvp',
            name='email',
            field=models.EmailField(max_length=75, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rsvp',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rsvp',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rsvp',
            name='number_of_guests',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
