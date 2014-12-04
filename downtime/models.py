from django.db import models
from django.contrib.auth.models import User
import reversion

class Influence(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Population(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Discipline(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
            return self.name

class Title(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
            return self.name

class Age(models.Model):
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
    titles = models.ManyToManyField(Title, blank=True)
    age = models.ForeignKey(Age)
    resources = models.IntegerField()

    def __str__(self):
        return self.name

class Debt(models.Model):
    count = models.IntegerField()
    size = models.ForeignKey(Boon)
    creditor = models.ForeignKey(Character, related_name='credits')
    debtor = models.ForeignKey(Character, related_name='debts')
    description = models.TextField()

    def __str__(self):
        return '%s owes %s: %d %s' % (self.debtor, self.creditor, self.count, self.size)

class Domain(models.Model):
    name = models.CharField(max_length=200)
    feeding_capacity = models.IntegerField()
    status = models.TextField()
    influence = models.TextField()
    masquerade = models.TextField()
    population = models.ForeignKey(Population)

    def __str__(self):
        return self.name

class ActionType(models.Model):
    name = models.CharField(max_length=200)
    template = models.TextField()

    def __str__(self):
        return self.name

class InfluenceRating(models.Model):
    influence = models.ForeignKey(Influence)
    rating = models.IntegerField()
    character = models.ForeignKey(Character, related_name='influences')

    def __str__(self):
        return '[%s]%s: %i' % (self.characted, self.influence, self.rating)

# Session actions
class Session(models.Model):
    name = models.CharField(max_length=200)
    is_open = models.BooleanField(default=True)
    feeding_domains = models.ManyToManyField(Domain, blank=True)                # finns det risk
    active_character = models.ManyToManyField(Character, blank=True)

    def __str__(self):
            return self.name

class Action(models.Model):
    action_type = models.ForeignKey(ActionType)
    character = models.ForeignKey(Character)
    session = models.ForeignKey(Session, related_name='actions')
    description = models.TextField()

    def __str__(self):
        return '[s] %s' % (self.character, self.action_type)

class Feeding(models.Model):
    character = models.ForeignKey(Character)
    session = models.ForeignKey(Session, related_name='feedings')
    domain = models.ForeignKey(Domain)
    feeding_points = models.IntegerField()
    discipline = models.ForeignKey(Discipline)
    description = models.TextField()

    def __str__(self):
        return '%s feeds %d in %s' (self.character, self.feeding_points, self.domain)

class BloodSpending(models.Model):
    character = models.ForeignKey(Character)
    session = models.ForeignKey(Session, related_name='blood_spending')
    active_disciples = models.ManyToManyField(Discipline, blank=True) # checka om de har disciplinerna

    def __str__(self):
        return
