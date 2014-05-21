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


def user_registered_callback(sender, user, request, **kwargs):
    profile = UserProfile(user=user)
    profile.address = request.POST["address"]
    profile.is_owner = bool(request.POST["is_owner"])
    profile.save()

user_registered.connect(user_registered_callback)
