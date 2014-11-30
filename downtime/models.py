from django.db import models
from django.contrib.auth.models import User

# Characters models
class Discipline(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
            return self.name

class Title(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
            return self.name

class Ability(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
            return self.name

class Boon(models.Model):
    name = models.CharField(max_length=200)
    value = models.IntegerField()

    def __str__(self):
            return self.name

class Character(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    disciplines = models.ManyToManyField(Discipline, blank=True)
    abilities = models.ManyToManyField(Ability, blank=True)
    titles = models.ManyToManyField(Title, blank=True)

    def __str__(self):
            return self.name

class Debt(models.Model):
    count = models.IntegerField()
    size = models.ForeignKey(Boon)
    creditor = models.ForeignKey(Character, related_name="credits")
    debtor = models.ForeignKey(Character, related_name="debts")
    description = models.TextField()

    def __str__(self):
            return "%s owes %s: %d %s" % (self.debtor, self.creditor, self.count, self.size)
