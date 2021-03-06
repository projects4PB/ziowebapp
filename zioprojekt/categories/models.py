from django.db import models


class TouristObjectsCategory(models.Model):
    """Tourist objects category class"""
    name = models.CharField(max_length=50, verbose_name=u'nazwa')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Kategoria'
        verbose_name_plural = u'Kategorie'
