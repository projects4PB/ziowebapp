# -*- coding: utf-8 -*-
from django.db import models

from .managers import TouristObjectManager


class Facilities(models.Model):
    """Facilities model"""
    name = models.CharField(max_length=255, verbose_name=u'nazwa')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'udogodnienie'
        verbose_name_plural = u'udogodnienia'


class TouristObjectsCity(models.Model):
    """Tourist objects city"""
    name = models.CharField(max_length=255, verbose_name=u'nazwa')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'miejscowość'
        verbose_name_plural = u'miejscowości'


class TouristObject(models.Model):
    """Tourist object model"""
    owner = models.ForeignKey(
        'accounts.UserProfile', verbose_name=u'właściciel ośrodka')
    name = models.CharField(max_length=255, verbose_name=u'nazwa')
    description = models.TextField(verbose_name=u'opis obiektu')
    facilities = models.ManyToManyField(
        Facilities, verbose_name=u'udogodnienia', blank=True)
    category = models.ForeignKey(
        'categories.TouristObjectsCategory',
        verbose_name=u'kategoria'
    )
    address = models.CharField(
        max_length=255, verbose_name=u'adres', blank=True)
    city = models.ForeignKey(
        TouristObjectsCity, verbose_name=u'miejscowość')
    creation_date = models.DateTimeField(
        auto_now_add=True, verbose_name=u'data utworzenia')

    objects = TouristObjectManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'obiekt turystyczny'
        verbose_name_plural = u'obiekty turystyczne'
