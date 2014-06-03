# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

from registration.signals import user_registered


class UserProfile(models.Model):
    user = models.ForeignKey(
        User, unique=True, verbose_name=u'użytkownik')
    address = models.CharField(
        max_length=255, verbose_name=u'adres',
        blank=True, null=True)
    is_owner = models.BooleanField(
        verbose_name=u'właściciel obiektu')

    def __unicode__(self):
        return self.user.username

    def is_participant(self, event):
        if self in event.participants.all():
            return True
        return False

    def is_moderator(self, event):
        if self == event.moderator:
            return True
        return False


def user_registered_callback(sender, user, request, **kwargs):
    profile = UserProfile(user=user)
    profile.address = request.POST["address"]
    if request.POST["is_owner"] == u'True':
        profile.is_owner = True
    else:
        profile.is_owner = False
    profile.save()

user_registered.connect(user_registered_callback)
