from django.db import models


class Offer(models.Model):
    """Offer model"""
    name = models.CharField(max_length=255, verbose_name=u'nazwa')
    tourist_object = models.ForeignKey(
        'places.TouristObject', verbose_name=u'powiązany obiekt')
    description = models.TextField(verbose_name=u'opis oferty')
    creation_date = models.DateTimeField(
        auto_now_add=True, verbose_name=u'data utworzenia')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Oferta'
        verbose_name_plural = u'Oferty'
