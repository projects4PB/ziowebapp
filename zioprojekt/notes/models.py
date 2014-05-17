from django.db import models


class Note(models.Model):
    """Note model"""
    author = models.ForeignKey('registration.RegistrationProfile',
                               verbose_name=u'autor')
    event = models.ForeignKey('events.Event', verbose_name=u'wydarzenie')
    title = models.CharField(max_length=255, verbose_name=u'tytuł')
    content = models.TextField(verbose_name=u'treść')

    def __unicode__(self):
        return self.title
