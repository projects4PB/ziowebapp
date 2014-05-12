from django.db import models


class TouristObjectsCategory(models.Model):
    """Tourist objects category class"""
    name = models.CharField(max_length=50, verbose_name=u'nazwa')
