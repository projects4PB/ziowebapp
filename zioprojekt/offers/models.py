# -*- coding: utf-8 -*-
from django.db import models

from djorm_pgfulltext.models import SearchManager
from djorm_pgfulltext.fields import VectorField


class Offer(models.Model):
    """Offer model"""
    name = models.CharField(max_length=255, verbose_name=u'nazwa')
    tourist_object = models.ForeignKey(
        'places.TouristObject', verbose_name=u'powiązany obiekt')
    description = models.TextField(verbose_name=u'opis oferty')
    price = models.IntegerField(verbose_name=u'cena', default=0)
    creation_date = models.DateTimeField(
        auto_now_add=True, verbose_name=u'data utworzenia')

    search_index = VectorField()

    objects = SearchManager(
        fields=('name', 'description'),
        auto_update_search_field=True
    )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Oferta'
        verbose_name_plural = u'Oferty'
