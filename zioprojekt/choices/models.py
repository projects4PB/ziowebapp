from django.db import models


class TripTypeChoice(models.Model):
    """Category choice model"""
    SLUG_CHOICES = (
        ('couple-trip', 'Wyjazd we dwoje'),
        ('friends-trip', 'Wyjazd ze znajomymi'),
        ('family-trip', 'Wyjazd z rodziną')
    )
    slug = models.CharField(
        max_length=15, choices=SLUG_CHOICES, verbose_name=u'slug')
    category = models.ManyToManyField(
        'categories.TouristObjectsCategory',
        verbose_name=u'kategorie')
    facilities = models.ManyToManyField(
        'places.Facilities', verbose_name=u'udogodnienia', blank=True)

    def __unicode__(self):
        return self.slug
