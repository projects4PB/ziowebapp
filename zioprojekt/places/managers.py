# -*- coding: utf-8 -*-
from django.db import models


class TouristObjectManager(models.Manager):

    def user_objs(self, profile):
        return self.filter(owner__exact=profile)
