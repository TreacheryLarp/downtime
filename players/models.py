from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

# Resolved states
UNRESOLVED = 'UNRESOLVED'
RESOLVED = 'RESOLVED'
PENDING = 'PENDING'
NO_ACTIONS = 'NO_ACTIONS'

# Rumor Types
RUMOR_UNRELIABLE = 'Unreliable'
RUMOR_RELIABLE = 'Reliable'
RUMOR_FACT = 'Fact'
RUMOR_VAMPIRE = 'Vampire'


class ActionType(models.Model):
    name = models.CharField(max_length=200)
    template = models.TextField(blank=True)
    history = HistoricalRecords()

    def help_texts():
        help_texts = []
        for action_type in ActionType.objects.order_by('name').all():
            if action_type.template:
                help_texts.append({
                    'title': action_type.name,
                    'text': action_type.template
                })
        return help_texts

    def __str__(self):
        return self.name


class ActionOption(models.Model):
    action_types = models.ManyToManyField(ActionType)
    count = models.PositiveIntegerField()
    history = HistoricalRecords()

    def __str__(self):
        action_types = ' or '.join(a.name for a in self.action_types.all())
        return '[%s]x%i' % (action_types, self.count)


class Influence(models.Model):
    name = models.CharField(max_length=200)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class Population(models.Model):
    name = models.CharField(max_length=200)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class Discipline(models.Model):
    name = models.CharField(max_length=200)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    action_options = models.ManyToManyField(ActionOption, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class Age(models.Model):
    name = models.CharField(max_length=200)
    action_options = models.ManyToManyField(ActionOption, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class Clan(models.Model):
    name = models.CharField(max_length=200)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User,
                                related_name='character',
                                blank=True,
                                null=True)
    disciplines = models.ManyToManyField(Discipline, blank=True)
    titles = models.ManyToManyField(Title, blank=True)
    age = models.ForeignKey(Age)
    resources = models.PositiveIntegerField()
    clan = models.ForeignKey(Clan)
    history = HistoricalRecords()

    def __str__(self):
        return '%s (%s)' % (self.name, self.user)

    def action_count(self, session):
        action_options = self.actions(session)
        count = 0
        for action_option in action_options:
            count += action_option.count
        return count

    def actions(self, session):
        action_options = list(self.age.action_options.all())
        extra_actions = ExtraAction.objects.filter(character=self,
                                                   session=session)
        for extra_action in extra_actions:
            action_options.extend(extra_action.action_options.all())
        for title in self.titles.all():
            action_options.extend(list(title.action_options.all()))
        return action_options

    def submitted(self, session):
        actions = Action.objects.filter(character=self, session=session)
        feedings = Feeding.objects.filter(character=self, session=session)
        active_disciplines = ActiveDisciplines.objects.filter(character=self,
                                                              session=session)
        if len(actions) + len(feedings) + len(active_disciplines) > 0:
            return {'disc': active_disciplines,
                    'feed': feedings,
                    'actions': actions}
        else:
            return False

    def resource_income(self):
        ratings = InfluenceRating.objects.filter(character=self)
        weights = [1, 5, 10]
        income = 0
        for rating in ratings:
            income += weights[min(rating.rating, 3) - 1]
        return income


class Domain(models.Model):
    name = models.CharField(max_length=200)
    feeding_capacity = models.PositiveIntegerField()
    status = models.CharField(max_length=200)
    influence = models.CharField(max_length=200)
    masquerade = models.CharField(max_length=200)
    population = models.ManyToManyField(Population, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        population = ', '.join(d.name for d in self.population.all())
        return '%s - FP: %s, S: %s, I: %s, M: %s, P: [%s]' % (
            self.name, self.feeding_capacity, self.status, self.influence,
            self.masquerade, population)


class InfluenceRating(models.Model):
    influence = models.ForeignKey(Influence)
    rating = models.PositiveIntegerField()
    character = models.ForeignKey(Character, related_name='influences')
    history = HistoricalRecords()

    def __str__(self):
        return '[%s] %s: %i' % (self.character, self.influence, self.rating)


# Session actions
class Session(models.Model):
    name = models.CharField(max_length=200)
    is_open = models.BooleanField(default=True)
    feeding_domains = models.ManyToManyField(Domain, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return '[%s] %s' % ('open' if self.is_open else 'closed', self.name)

    def submitted(self):
        return [i for i in list(Character.objects.all()) if i.submitted(self)]

    def resolved_state(self, character):
        """
            Checks all actions and feedings,
            priority is pending > unresolved > resolved
        """
        state = RESOLVED
        actions = list(Action.objects.filter(character=character,
                                             session=self))
        actions.extend(list(Feeding.objects.filter(character=character,
                                                   session=self)))
        if len(actions) == 0:
            return NO_ACTIONS
        for a in actions:
            if a.resolved == PENDING:
                return a.resolved
            elif a.resolved == UNRESOLVED:
                state = UNRESOLVED
        return state


class Action(models.Model):
    action_type = models.ForeignKey(ActionType)
    character = models.ForeignKey(Character)
    session = models.ForeignKey(Session, related_name='actions')
    description = models.TextField()
    resolved = models.CharField(
        max_length=10,
        choices=((UNRESOLVED, 'Unresolved'), (PENDING, 'Pending'), (
            RESOLVED, 'Resolved')),
        default=UNRESOLVED)
    history = HistoricalRecords()

    def __str__(self):
        return '[%s] %s: %s' % (self.session.name, self.character,
                                self.action_type)


class Feeding(models.Model):
    character = models.ForeignKey(Character)
    session = models.ForeignKey(Session, related_name='feedings')
    domain = models.ForeignKey(Domain)
    feeding_points = models.PositiveIntegerField()
    discipline = models.ForeignKey(Discipline, blank=True, null=True)
    description = models.TextField()
    resolved = models.CharField(
        max_length=10,
        choices=((UNRESOLVED, 'Unresolved'), (PENDING, 'Pending'), (
            RESOLVED, 'Resolved')),
        default=UNRESOLVED)
    history = HistoricalRecords()

    def __str__(self):
        return '[%s] %s: %d in %s' % (self.session.name, self.character,
                                      self.feeding_points, self.domain)

    def is_overfeeding(self):
        feedings = list(Feeding.objects.filter(session=self.session,
                                               domain=self.domain))
        sum = 0
        for feeding in feedings:
            sum += feeding.feeding_points
            if sum > self.domain.feeding_capacity:
                return True

        return False


class ActiveDisciplines(models.Model):
    character = models.ForeignKey(Character)
    session = models.ForeignKey(Session, related_name='active_disciplines')
    disciplines = models.ManyToManyField(Discipline, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        disciplines = ', '.join(d.name for d in self.disciplines.all())
        return '[%s] %s: %s' % (self.session.name, self.character, disciplines)


class ExtraAction(models.Model):
    character = models.ForeignKey(Character, related_name='+')
    session = models.ForeignKey(Session, related_name='+')
    action_options = models.ManyToManyField(ActionOption)
    description = models.TextField()
    history = HistoricalRecords()

    def __str__(self):
        action_options = ', '.join(str(d) for d in self.action_options.all())
        return '[%s] +%s to %s' % (self.session.name, action_options,
                                   self.character)


class Rumor(models.Model):
    influence = models.ForeignKey(Influence)
    session = models.ForeignKey(Session, related_name='rumors')
    recipients = models.ManyToManyField(Character,
                                        blank=True,
                                        related_name='rumors')
    description = models.TextField()
    gm_note = models.TextField(blank=True)
    rumor_type = models.CharField(
        max_length=15,
        choices=((RUMOR_UNRELIABLE, 'Unreliable'), (
            RUMOR_RELIABLE, 'Reliable'), (RUMOR_FACT, 'Fact'), (RUMOR_VAMPIRE,
                                                                'Vampire')),
        default=RUMOR_UNRELIABLE)

    def __str__(self):
        return '[%s] %s - %s: %s' % (self.session.name, self.influence,
                                     self.rumor_type, self.description)
