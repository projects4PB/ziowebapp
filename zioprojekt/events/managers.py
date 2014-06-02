# -*- coding: utf-8 -*-
from django.db import models


class EventManager(models.Manager):

    def user_events(self, profile):
        related_events = []
        for event in self.all():
            if profile in event.participants.all():
                related_events.append(event)

        return related_events


class EventJoinOfferManager(models.Manager):
    def active(self):
        return self.filter(accepted=False)
