from django.db import models


class NoteManager(models.Manager):

    def get_for_user(self, user):
        return self.all().filter(
            author__user__exact=user)
