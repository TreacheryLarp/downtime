from django.db import models
from django.contrib.auth.models import User
import reversion


class ActionType(models.Model):
    name = models.CharField(max_length=200)
    template = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ActionOption(models.Model):
    action_types = models.ManyToManyField(ActionType)
    count = models.PositiveIntegerField()

    def __str__(self):
        return '%s x%i' % (self.action_types.all(), self.count)


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
    action_options = models.ManyToManyField(ActionOption, blank=True)

    def __str__(self):
            return self.name


class Age(models.Model):
    name = models.CharField(max_length=200)
    action_options = models.ManyToManyField(ActionOption, blank=True)

    def __str__(self):
            return self.name


class Boon(models.Model):
    name = models.CharField(max_length=200)
    value = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Clan(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User, related_name='character')
    disciplines = models.ManyToManyField(Discipline, blank=True)
    titles = models.ManyToManyField(Title, blank=True)
    age = models.ForeignKey(Age)
    resources = models.PositiveIntegerField()
    clan = models.ForeignKey(Clan)

    def __str__(self):
        return self.name

    def action_count(self):
        action_options = self.actions()
        count = 0
        for action_option in action_options:
            count += action_option.count
        return count

    def actions(self):
        action_options = list(self.age.action_options.all())
        for title in self.titles.all():
            action_options.extend(list(title.action_options.all()))
        return action_options


class Debt(models.Model):
    count = models.PositiveIntegerField()
    size = models.ForeignKey(Boon)
    creditor = models.ForeignKey(Character, related_name='credits')
    debtor = models.ForeignKey(Character, related_name='debts')
    description = models.TextField()

    def __str__(self):
        return '%s owes %s: %d %s' % (self.debtor, self.creditor, self.count, self.size)


class Domain(models.Model):
    name = models.CharField(max_length=200)
    feeding_capacity = models.PositiveIntegerField()
    status = models.TextField()
    influence = models.TextField()
    masquerade = models.TextField()
    population = models.ForeignKey(Population)

    def __str__(self):
        return self.name


class InfluenceRating(models.Model):
    influence = models.ForeignKey(Influence)
    rating = models.PositiveIntegerField()
    character = models.ForeignKey(Character, related_name='influences')

    def __str__(self):
        return '[%s]%s: %i' % (self.character, self.influence, self.rating)


# Session actions
class Session(models.Model):
    name = models.CharField(max_length=200)
    is_open = models.BooleanField(default=True)
    feeding_domains = models.ManyToManyField(Domain, blank=True)

    def __str__(self):
        return self.name


class Action(models.Model):
    action_type = models.ForeignKey(ActionType)
    character = models.ForeignKey(Character)
    session = models.ForeignKey(Session, related_name='actions')
    description = models.TextField()

    def __str__(self):
        return '[%s] %s' % (self.character, self.action_type)


class Feeding(models.Model):
    character = models.ForeignKey(Character)
    session = models.ForeignKey(Session, related_name='feedings')
    domain = models.ForeignKey(Domain)
    feeding_points = models.PositiveIntegerField()
    discipline = models.ForeignKey(Discipline)
    description = models.TextField()

    def __str__(self):
        return '%s feeds %d in %s' % (self.character, self.feeding_points, self.domain)


class ActiveDisciplines(models.Model):
    character = models.ForeignKey(Character)
    session = models.ForeignKey(Session, related_name='active_disciplines')
    disciplines = models.ManyToManyField(Discipline, blank=True)

    def __str__(self):
        return '[%s] %s: %s' % (self.session, self.character, self.disciplines.all())
