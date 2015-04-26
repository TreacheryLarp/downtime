from base64 import b32encode
from hashlib import sha1
from random import random

from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

from players.models import Session, Character


class BoonSize(models.Model):
    name = models.CharField(max_length=200)
    value = models.PositiveIntegerField()
    history = HistoricalRecords()

    def __str__(self):
        return '%s' % self.name


class Boon(models.Model):

    is_activated = models.BooleanField(default=False)
    debtor = models.ForeignKey(Character, related_name='credits')
    creditor = models.ForeignKey(Character, related_name='debits')
    size = models.ForeignKey(BoonSize)
    description = models.TextField()
    history = HistoricalRecords()

    def __str__(self):
        return '[%s] %s' % (self.key, self.debtor)
