# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models

from .managers import EventManager


class Event(models.Model):
    """Note model"""
    moderator = models.ForeignKey('accounts.UserProfile',
                                  verbose_name=u'moderator')
    participants = models.ManyToManyField('accounts.UserProfile',
                                          related_name='event_participants',
                                          verbose_name=u'uczestnicy',
                                          blank=True, null=True)
    offer = models.ForeignKey('offers.Offer', verbose_name=u'oferta')
    name = models.CharField(max_length=255, verbose_name=u'nazwa')
    description = models.TextField(verbose_name=u'treść',
                                   blank=True, null=True)
    creation_date = models.DateTimeField(
        auto_now_add=True, verbose_name=u'data utworzenia')
    objects = EventManager()

    def get_absolute_url(self):
        return reverse('show_event', args=[str(self.id)])

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Wydarzenie'
        verbose_name_plural = u'Wydarzenia'
