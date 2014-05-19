from django.db import models


class Event(models.Model):
    """Note model"""
    moderator = models.ForeignKey('registration.RegistrationProfile',
                                  verbose_name=u'moderator')
    participants = models.ManyToManyField('registration.RegistrationProfile',
                                          related_name='event_participants',
                                          verbose_name=u'uczestnicy',
                                          blank=True, null=True)
    offer = models.ForeignKey('offers.Offer', verbose_name=u'oferta')
    name = models.CharField(max_length=255, verbose_name=u'nazwa')
    description = models.TextField(verbose_name=u'treść',
                                   blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Wydarzenie'
        verbose_name_plural = u'Wydarzenia'
