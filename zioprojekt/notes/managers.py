from django.db import models


class NoteManager(models.Manager):

    def get_for_user(self, user):
        return self.all().filter(
            author__user__exact=user)

    def event_notes(self, event):
        return self.all().filter(
            event=event)
