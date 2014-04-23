from django.db import models


class Note(models.Model):
    text = models.TextField()
    number = models.IntegerField()
    blob = models.BinaryField()
