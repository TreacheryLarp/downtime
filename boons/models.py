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


class Transaction(models.Model):
    creditor = models.ForeignKey(Character, related_name='credits')
    transaction_time = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return '%s' % self.creditor


class Boon(models.Model):

    def pkgen():
        while True:
            # Use secure random? Not really needed though..
            pk = b32encode(sha1(str(random())).digest()).lower()[:5]
            if len(Boon.objects.filter(key=pk)) == 0:
                return pk

    is_activated = models.BooleanField(default=False)
    key = models.CharField(max_length=5, primary_key=True, default=pkgen)
    debtor = models.ForeignKey(Character, related_name='boons')
    size = models.ForeignKey(BoonSize)
    active_transaction = models.ForeignKey(Transaction, blank=True, related_name='+')
    transactions = models.ManyToManyField(Transaction, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return '[%s] %s' % (self.key, self.debtor)
