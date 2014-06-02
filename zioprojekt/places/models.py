# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models

from djangoratings.fields import RatingField

from database_storage import DatabaseStorage

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
    rating = RatingField(range=5, verbose_name=u'ocena')

    objects = TouristObjectManager()

    def get_absolute_url(self):
        return reverse('tourist_object_detail', args=[str(self.id)])

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'obiekt turystyczny'
        verbose_name_plural = u'obiekty turystyczne'


class TouristObjectImage(models.Model):
    DBS_OPTIONS = {
        'table': 'places_images',
        'base_url': '/storage_images/',
    }

    tourist_object = models.ForeignKey(
        TouristObject, verbose_name=u'obiekt turystyczny')
    image = models.ImageField(upload_to='places/',
                              storage=DatabaseStorage(DBS_OPTIONS),
                              verbose_name=u'zdjęcie')
    caption = models.CharField(max_length=255, verbose_name=u'podpis',
                               blank=True, null=True)

    def __unicode__(self):
        return self.caption

    class Meta:
        verbose_name = u'zdjęcie obiektu'
        verbose_name_plural = u'zdjęcia obiektów'
