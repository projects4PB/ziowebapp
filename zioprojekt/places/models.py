from django.db import models

from djorm_pgfulltext.models import SearchManager
from djorm_pgfulltext.fields import VectorField


class Facilities(models.Model):
    """Facilities model"""
    name = models.CharField(max_length=255, verbose_name=u'nazwa')

    def __unicode__(self):
        return self.name


class TouristObjectsCity(models.Model):
    """Tourist objects city"""
    name = models.CharField(max_length=255, verbose_name=u'nazwa')

    def __unicode__(self):
        return self.name


class TouristObject(models.Model):
    """Tourist object abstract model"""
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

    class Meta:
        abstract = True


class HolidayCamp(TouristObject):
    """Holiday camp model"""

    class Meta:
        verbose_name = u'ośrodek letniskowy'


class RestCentre(TouristObject):
    """Rest centre model"""
    search_index = VectorField()

    objects = SearchManager(
        fields=('name', 'description'),
        auto_update_search_field=True
    )

    class Meta:
        verbose_name = u'ośrodek wczasowy'


class Hotel(TouristObject):
    """Hotel model"""

    class Meta:
        verbose_name = u'hotel'


class Motel(TouristObject):
    """Motel model"""

    class Meta:
        verbose_name = u'motel'


class Camping(TouristObject):
    """Camping model"""

    class Meta:
        verbose_name = u'camping'


class GuestHouse(TouristObject):
    """Guest house model"""

    class Meta:
        verbose_name = u'pensjonat'
