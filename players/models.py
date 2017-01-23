from django.db import models
from django.db.models import *
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


class ActionType(Model):
    name = CharField(max_length=200)
    template = TextField(blank=True)
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


class ActionOption(Model):
    action_types = ManyToManyField(ActionType)
    count = PositiveIntegerField()
    history = HistoricalRecords()

    def __str__(self):
        action_types = ' or '.join(a.name for a in self.action_types.all())
        return '[{}]{}'.format(action_types, self.count)


class Influence(Model):
    name = CharField(max_length=200)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class Population(Model):
    name = CharField(max_length=200)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

class ElderPower(Model):
    name = CharField(max_length=200)
    history = HistoricalRecords()
    description = TextField()

    def __str__(self):
        return self.name


class Discipline(Model):
    name = CharField(max_length=200)
    history = HistoricalRecords()

    def __str__(self):
        return self.name
        
class DisciplineRating(Model):
    discipline = ForeignKey(Discipline, null=True, blank=True)
    value = PositiveIntegerField(default=1)
    elder_powers = ManyToManyField(ElderPower, blank=True)
    learned = BooleanField(default=False)
    elder_blood = BooleanField(default=False)
    in_clan = BooleanField(default=False)
    mentor = BooleanField(default=False)
    exp = PositiveIntegerField(default=0)    
    history = HistoricalRecords()

    def __str__(self):
        return '{} {}'.format(self.discipline.name, str(self.value))
        

class Attribute(Model):
    name = CharField(max_length=200)
    history = HistoricalRecords()

    def __str__(self):
        return self.name
        
class AttributeRating(Model):
    attribute = ForeignKey(Attribute, null=True, blank=True)
    learned = BooleanField(default=False)
    elder_blood = BooleanField(default=False)
    mentor = BooleanField(default=False)
    value = PositiveIntegerField(default=1)
    exp = PositiveIntegerField(default=0)    
    history = HistoricalRecords()

    def __str__(self):
        return  '{} {}'.format(self.attribute.name, str(self.value))

class Specialization(Model):
    name = CharField(max_length=200)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

class Weapon(Model):
    name = CharField(max_length=200)
    mod = PositiveIntegerField()
    damage_types = (("bash","bash"),("lethal","lethal"),("aggrevated","aggrevated"))
    damage_type = CharField(max_length=200,choices = damage_types)
    resources = PositiveIntegerField()
    ranged = BooleanField(default=False)
    history = HistoricalRecords()

    def __str__(self):
        return '{} (cost {}, bonus {} {} {})'.format(
            self.name,
            self.resources,
            self.mod,
            self.damage_type,
            "ranged" if self.ranged else ""
            )

class Title(Model):
    name = CharField(max_length=200)
    action_options = ManyToManyField(ActionOption, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

class Age(Model):
    name = CharField(max_length=200)
    action_options = ManyToManyField(ActionOption, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

class Clan(Model):
    name = CharField(max_length=200)
    theme = TextField(blank=True)
    history = HistoricalRecords()
    clan_disciplines = ManyToManyField(Discipline, blank=True)

    def __str__(self):
        return self.name

class PoliticalFaction(Model):
    name = CharField(max_length=200)
    description = TextField(blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name
        
class CanonFact(Model):
    name = CharField(max_length=200)
    description = TextField()
    history = HistoricalRecords()

    def __str__(self):
        return self.name        
        
class Nature(Model):
    name = CharField(max_length=200)
    history = HistoricalRecords()

    def __str__(self):
        return self.name        
        
class Relationship(Model):
    character = ForeignKey('Character', related_name='relationship')
    complicated = BooleanField()
    description = TextField()
    blood_bond = PositiveIntegerField(choices=((0,0),(1,1),(2,2),(3,3)),default=0)
    history = HistoricalRecords()

    def __str__(self):
        return 'to {}' .format(self.character.name)

class Ritual(Model):
    name = CharField(max_length=200)
    level = PositiveIntegerField(default=1)
    description = TextField()
    history = HistoricalRecords()

    def __str__(self):
        return self.name

class RitualRating(Model):
    ritual = ForeignKey(Ritual)
    exp = BooleanField(default=False)
    invested = PositiveIntegerField(default=0)    
    history = HistoricalRecords()

    def __str__(self):
        return '{} {}'.format(self.ritual.name, str(self.invested))

class HookAttribute(Model):
    name = CharField(max_length=200)
    history = HistoricalRecords()

    def __str__(self):
        return self.name        
        
class Hook(Model):
    name = CharField(max_length=200)
    influence = ForeignKey(Influence)
    attributes = ManyToManyField(HookAttribute,blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name
        
class Boon(Model):
    signer = ForeignKey('Character')
    SIZE_CHOICES = (
      ('trivial', 'trivial'),
      ('liten', 'liten'),
      ('enkel', 'enkel'),
      ('stor', 'stor'),
      ('livs', 'livs'),
    ) 
    size = CharField(choices=SIZE_CHOICES,max_length=10,default="enkel")
    number = PositiveIntegerField(default=1)
    history = HistoricalRecords()
    def __str__(self):
        return str(self.number) +" "+self.size + " från " + self.signer.name          
        
        
      
class Equipment(Model):
  name = CharField(max_length=200)
  specialization = ForeignKey(Specialization,null=True,blank=True)
  
  def __str__(self):
        return self.name 
  
class Ghoul(Model):
  name = CharField(max_length=200)
  level = PositiveIntegerField(choices=((1,1),(2,2),(3,3)),default=1)
  hook = OneToOneField(Hook,blank=True,null=True)
  disciplines = ManyToManyField(DisciplineRating, blank=True)
  specializations = ManyToManyField(Specialization, blank=True)
  
  def __str__(self):
        return self.name    
   
class Character(Model):
    name = CharField(max_length=200)
    user = OneToOneField(
                        User,
                        related_name='character',
                        blank=True,
                        null=True)
    disciplines = ManyToManyField(DisciplineRating,   blank=True)
    attributes  = ManyToManyField(AttributeRating,    blank=True)
    rituals     = ManyToManyField(RitualRating,       blank=True)
    specializations = ManyToManyField(Specialization, blank=True)
    hooks  = ManyToManyField(Hook,  blank=True)
    titles = ManyToManyField(Title, blank=True)
    boons  = ManyToManyField(Boon,  blank=True)
    canon_fact        = ManyToManyField(CanonFact, blank=True)
    political_faction = ForeignKey(PoliticalFaction, blank=True,null=True)
    age     = ForeignKey(Age)
    clan    = ForeignKey(Clan,blank=True,null=True)
    nature  = ForeignKey(Nature,related_name='+')
    demeanor= ForeignKey(Nature,related_name='+')
    sire    = ForeignKey('Character',blank=True,null=True)
    concept = TextField(blank=True)
        
    open_goal1  = TextField(blank=True)
    open_goal2  = TextField(blank=True)
    hidden_goal = TextField(blank=True)
    
    relationships = ManyToManyField(Relationship, related_name='master', blank=True)
    
    frenzyTriggers = TextField(blank=True)
    
    herd  = PositiveIntegerField(choices=((0,0),(1,1),(2,2),(3,3)),default=0)
    haven = PositiveIntegerField(choices=((0,0),(1,1),(2,2),(3,3)),default=0)
    ghouls    = ManyToManyField(Ghoul,     blank=True)
    equipment = ManyToManyField(Equipment, blank=True)
    weapons   = ManyToManyField(Weapon,    blank=True)
        
    exp          = PositiveIntegerField(default=0)
    humanity_exp = PositiveIntegerField(default=0)
    special_exp  = PositiveIntegerField(default=0)
    
    health     = PositiveIntegerField(default=7)
    blood      = PositiveIntegerField(default=10)
    humanity   = PositiveIntegerField(default=7)
    willpower  = PositiveIntegerField(default=0)
    resources  = PositiveIntegerField(default=0)
    generation = PositiveIntegerField(default=13)  
    
    additional_notes = TextField(blank=True)
          
    history = HistoricalRecords()

    def __str__(self):
        return '{} ({})'.format(self.name, self.user)   

    def action_count(self, session):
        action_options = self.actions(session)
        count = 0
        for action_option in action_options:
            count += action_option.count
        return count

    def actions(self, session):
        action_options = list(self.age.action_options.all())
        extra_actions  = ExtraAction.objects.filter(character=self, session=session)
        for extra_action in extra_actions:
            action_options.extend(extra_action.action_options.all())
        for title in self.titles.all():
            action_options.extend(list(title.action_options.all()))
        return action_options

    def submitted(self, session):
        actions  = Action.objects.filter(character=self, session=session)
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


class Domain(Model):
    name = CharField(max_length=200)
    feeding_capacity = PositiveIntegerField()
    status = CharField(max_length=200)
    influence = CharField(max_length=200)
    masquerade = CharField(max_length=200)
    population = ManyToManyField(Population, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        population = ', '.join(d.name for d in self.population.all())
        return '{} - FP: {}, S: {}, I: {}, M: {}, P: [{}]'.format(
            self.name, self.feeding_capacity, self.status, self.influence,
            self.masquerade, population)


class InfluenceRating(Model):
    influence = ForeignKey(Influence)
    rating = PositiveIntegerField()
    character = ForeignKey(Character, related_name='influences')
    history = HistoricalRecords()

    def __str__(self):
        return '[{}] {}: {:i}'.format(self.character, self.influence, self.rating)


# Session actions
class Session(Model):
    name = CharField(max_length=200)
    is_open = BooleanField(default=True)
    is_special = BooleanField(default=False)
    action_set = ForeignKey(ActionOption,blank=True,null=True)
    feeding_domains = ManyToManyField(Domain, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return '[{}] {}'.format('open' if self.is_open else 'closed', self.name)

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


class Action(Model):
    action_type = ForeignKey(ActionType)
    character = ForeignKey(Character)
    session = ForeignKey(Session, related_name='actions')
    helpers = ManyToManyField(Character,related_name="allowedHelp", blank=True)
    willpower = BooleanField(default=False)
    description = TextField(blank=True)
    resolved = CharField(
        max_length=10,
        choices=((UNRESOLVED, 'Unresolved'), (PENDING, 'Pending'), (
            RESOLVED, 'Resolved')),
        default=UNRESOLVED)
    history = HistoricalRecords()

    def to_description(self):
        return '{} '.format(self.action_type)
    def __str__(self):
        return '[{}] {}: {}'.format(self.session.name, self.character,
                                self.action_type)
                                




                               
class AidAction(Action):
    helpee = ForeignKey(Character,related_name="help")
    action = ForeignKey(ActionType)
    name = CharField(max_length=200,blank=True)
    betrayal = BooleanField(default=False)
    def to_description(self):
        betrayal = '{} is betraying {}.' .format(
            self.character.
            name,self.helpee.name) 
        hook = 'on {}' .format(self.name) if self.name != "" else ""
        return '{} is helping {} with {} {}.\n {}' .format(            
            self.character.name,
            self.helpee.name,
            self.action.name,
            hook,
            betrayal if self.betrayal else ""
            )


class ConserveInfluence(Action): 
    influence = ForeignKey(Influence)
    def to_description(self):
        return '{} is conserving {}.'.format(            
            self.character.name,
            self.influence.name)

class ConserveDomain(Action): 
    domain = ForeignKey(Domain)
    def to_description(self):
        return '{} is conserving {}.'.format(            
            self.character.name,
            self.domain.name)

class InfluenceForge(Action): 
    name = CharField(max_length=200)
    influence = ForeignKey(Influence)
    def to_description(self):
        return '{} is forging {} in the influence {}.'.format(            
            self.character.name,
            self.name,
            self.influence.name)

class InfluenceSteal(Action): 
    name = CharField(max_length=200)
    influence = ForeignKey(Influence)
    def to_description(self):
        return '{} is stealing {} in the influence {}.'.format(            
            self.character.name,
            self.name,
            self.influence.name)

class InfluenceDestroy(Action): 
    name = CharField(max_length=200)
    influence = ForeignKey(Influence)
    def to_description(self):
        return '{} is destroying {} in the influence {}.'.format(            
            self.character.name,
            self.name,
            self.influence.name)
        
class InfluencePriority(Model):
    name = CharField(max_length=200)
    cost = PositiveIntegerField()
    influence = ForeignKey(Influence,blank=True,null=True)
    def __str__(self):
        influence = ' ({})'.format(self.influence.name) if self.influence != None else "" 
        return '{}{} {}'.format(self.name,influence, str(self.cost)) 
       
class InvestigateCharacterInfluence(Action): 
    target = ForeignKey(Character,related_name="investigate_influence")
    
   
    priority1 = ForeignKey(InfluencePriority,blank=True,null=True,related_name="priority1")
    priority2 = ForeignKey(InfluencePriority,blank=True,null=True,related_name="priority2")
    priority3 = ForeignKey(InfluencePriority,blank=True,null=True,related_name="priority3")
    priority4 = ForeignKey(InfluencePriority,blank=True,null=True,related_name="priority4")
    priority5 = ForeignKey(InfluencePriority,blank=True,null=True,related_name="priority5")
    priority6 = ForeignKey(InfluencePriority,blank=True,null=True,related_name="priority6")
    priority7 = ForeignKey(InfluencePriority,blank=True,null=True,related_name="priority7")
    priority8 = ForeignKey(InfluencePriority,blank=True,null=True,related_name="priority8")

    hooks = TextField(blank=True)
    def to_description(self):
        priorities = '{},{},{},{},{},{},{},{}' .format(
            self.priority1,
            self.priority2,
            self.priority3,
            self.priority4,
            self.priority5,
            self.priority6,
            self.priority7,
            self.priority8)
        return '{} is investigating {}\'s influence. \n Priorities: {} \n with hooks: {}'.format(            
            self.character.name,
            self.target.name,
            priorities,
            self.hooks)
    
class ResourcePriority(Model):
    name = CharField(max_length=200)
    cost = PositiveIntegerField()
    def __str__(self):       
        return '{} {}'.format(self.name, str(self.cost)) 

class InvestigateCharacterResources(Action): 
    target = ForeignKey(Character,related_name="investigate_resources")
  
    priority1 = ForeignKey(ResourcePriority,blank=True,null=True,related_name="priority1")
    priority2 = ForeignKey(ResourcePriority,blank=True,null=True,related_name="priority2")
    priority3 = ForeignKey(ResourcePriority,blank=True,null=True,related_name="priority3")
    priority4 = ForeignKey(ResourcePriority,blank=True,null=True,related_name="priority4")
    priority5 = ForeignKey(ResourcePriority,blank=True,null=True,related_name="priority5")
    priority6 = ForeignKey(ResourcePriority,blank=True,null=True,related_name="priority6")
    priority7 = ForeignKey(ResourcePriority,blank=True,null=True,related_name="priority7")
    priority8 = ForeignKey(ResourcePriority,blank=True,null=True,related_name="priority8")

    def to_description(self):
        priorities = '{},{},{},{},{},{},{},{}' .format(
            self.priority1,
            self.priority2,
            self.priority3,
            self.priority4,
            self.priority5,
            self.priority6,
            self.priority7,
            self.priority8)
        return '{} is investigating {}\'s resources. \n Priorities: {}'.format(
            self.character.name,
            self.target.name,
            priorities)
            
class InvestigateCharacterDowntimeActions(Action): 
    target = ForeignKey(Character,related_name="investigate_downtime_actions")
    def to_description(self):
        return '{} is investigating {}\'s downtime actions.'.format(
            self.character.name,
            self.target.name,
            )
    
class InvestigateCounterSpionage(Action):
    pass
    def to_description(self):
        return '{} is doing counter espionage.' .format(self.character.name)
    
class InvestigatePhenomenon(Action): 
    phenonemon = TextField()
    def to_description(self):
        return '{} is investigating: {}'.format(self.character.name,self.phenonemon)

class InvestigateInfluence(Action): 
    influence = ForeignKey(Influence)
    def to_description(self):
        return '{} is investigating {}.'.format(self.character.name,self.influence.name)

class LearnAttribute(Action): 
    attribute = ForeignKey(Attribute)
    trainer = ForeignKey(Character,
                         related_name="AttributeTrainee",blank=True,null=True)
    def to_description(self):
        teacher = 'With {} as teacher.' .format(self.trainer.name) if self.trainer != None else ""
        return '{} is learning {}. {}' .format(
            self.character.name,
            self.attribute.name,
            teacher)
    
class LearnDiscipline(Action): 
    discipline = ForeignKey(Discipline)
    trainer = ForeignKey(Character,related_name="DisciplineTrainee",blank=True,null=True)
    def to_description(self):
        teacher = 'With {} as teacher.' .format(self.trainer.name) if self.trainer != None else ""
        return '{} is learning {}. {}' .format(
            self.character.name,
            self.discipline.name,
            teacher)

class LearnSpecialization(Action): 
    new_specialization = ForeignKey(Specialization,related_name="learner")
    old_specialization = ForeignKey(Specialization,related_name="forgeter")
    trainer = ForeignKey(Character,related_name="SpecializationTrainee",blank=True,null=True)        
    def to_description(self):
        teacher = 'With {} as teacher.' .format(self.trainer.name) if self.trainer != None else ""
        return '{} is learning {},replacing {}. {}' .format(
            self.character.name,
            self.new_specialization.name,
            self.old_specialization.name,
            teacher)

class InvestGhoul(Action):
    name = CharField(max_length=200)
    discipline = ForeignKey(Discipline)
    specialization = ForeignKey(Specialization)
    def to_description(self):
        return '{} is investing in the ghoul {}, which is getting {} and {}.'.format(
            self.character.name,
            self.name,
            self.discipline.name,
            self.specialization.name)
  
class InvestEquipment(Action):
    name = CharField(max_length=200)
    specialization = ForeignKey(Specialization)
    def to_description(self):
        return '{} is investing in the equipment {}, which is used for {}.'.format(
            self.character.name,
            self.name,
            self.specialization.name)


class InvestWeapon(Action):
    weapon = ForeignKey(Weapon)
    def to_description(self):
        return '{} is investing in the weapon {}.'.format(            
            self.character.name,
            self.weapon.name)

class InvestHerd(Action):
    def to_description(self):
        return '{} is investing in their herd.'.format(
            self.character.name)
    
class InvestHaven(Action): 
    def to_description(self):
        return '{} is investing in their haven.'.format(
            self.character.name)

class MentorAttribute(Action): 
    attribute = ForeignKey(Attribute)
    student   = ForeignKey(Character,related_name="attribute_teacher")
    def to_description(self):
        return '{} is mentoring {} on {}.'.format(            
            self.character.name,
            self.student.name,
            self.attribute)

class MentorDiscipline(Action): 
    discipline = ForeignKey(Discipline)
    student    = ForeignKey(Character,related_name="discipline_teacher")
    def to_description(self):
        return '{} is mentoring {} on {}.'.format(            
            self.character.name,
            self.student.name,
            self.discipline)
            
class MentorSpecialization(Action): 
    specialization = ForeignKey(Specialization)
    student        = ForeignKey(Character,related_name="specialization_teacher")
    def to_description(self):
        return '{} is mentoring {} on {}.'.format(            
            self.character.name,
            self.student.name,
            self.specialization)

class Rest(Action):
    def to_description(self):
        return '{} is resting.' .format(self.character.name)
        
        
class NeglectDomain(Action):
    domain = ForeignKey(Domain)
    def to_description(self):
        return '{} is neglecting {}.' .format(
            self.character.name,
            self.domain.name)          
        
class PatrolDomain(Action):
    domain = ForeignKey(Domain)
    def to_description(self):
        return '{} is patroling {}.' .format(
            self.character.name,
            self.domain.name)        
            
class KeepersQuestion(Action):
    target = ForeignKey(Character)
    question = TextField()
    def to_description(self):
        return '{} asked their visitor {}: {}' .format(
            self.character.name,
            self.target.name,
            self.question) 

class PrimogensQuestion(Action):
    target = ForeignKey(Character)
    question = TextField()
    def to_description(self):
        return '{} asked their clanmember {}: {}' .format(
            self.character.name,
            self.target.name,
            self.question)
                               
class PrimogensAidAction(Action):
    helpee = ForeignKey(Character,related_name="primogen_help")
    action = ForeignKey(ActionType)
    name = CharField(max_length=200,blank=True)
    betrayal = BooleanField(default=False)
    def to_description(self):
        betrayal = '{} is betraying {}.' .format(
            self.character.
            name,self.helpee.name) 
        hook = 'on {}' .format(self.name) if self.name != "" else ""
        return '{} is helping their clanmember {} with {} {}.\n {}'.format(
            self.character.name,
            self.helpee.name,
            self.action.name,
            hook,
            betrayal if self.betrayal else "")

class Feeding(Model):
    character = ForeignKey(Character)
    session = ForeignKey(Session, related_name='feedings')
    domain = ForeignKey(Domain)
    feeding_points = PositiveIntegerField()
    discipline = ForeignKey(DisciplineRating, blank=True, null=True)
    description = TextField()
    resolved = CharField(
        max_length=10,
        choices=((UNRESOLVED, 'Unresolved'), (PENDING, 'Pending'), (
            RESOLVED, 'Resolved')),
        default=UNRESOLVED)
    history = HistoricalRecords()

    def __str__(self):
        return '[{}] {}: .formatd in {}'.format(
            self.session.name, 
            self.character,
            self.feeding_points, 
            self.domain)

    def is_overfeeding(self):
        feedings = list(Feeding.objects.filter(session=self.session,
                                               domain=self.domain))
        sum = 0
        for feeding in feedings:
            sum += feeding.feeding_points
            if sum > self.domain.feeding_capacity:
                return True

        return False




class ActiveDisciplines(Model):
    character = ForeignKey(Character)
    session = ForeignKey(Session, related_name='active_disciplines')
    disciplines = ManyToManyField(DisciplineRating, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        disciplines = ', '.join(d.name for d in self.disciplines.all())
        return '[{}] {}: {}'.format(self.session.name, self.character, disciplines)


class ExtraAction(Model):
    character = ForeignKey(Character, related_name='+')
    session = ForeignKey(Session, related_name='+')
    action_options = ManyToManyField(ActionOption)
    description = TextField()
    history = HistoricalRecords()

    def __str__(self):
        action_options = ', '.join(str(d) for d in self.action_options.all())
        return '[{}] +{} to {}'.format(self.session.name, action_options,
                                   self.character)


class Rumor(Model):
    influence = ForeignKey(Influence, blank=True,null=True)
    canonFact = ForeignKey(CanonFact, blank=True,null=True)
    session = ForeignKey(Session, related_name='rumors')
    recipients = ManyToManyField(Character,
                                        blank=True,
                                        related_name='rumors')
    description = TextField()
    gm_note = TextField(blank=True)
    rumor_type = CharField(
        max_length=15,
        choices=((RUMOR_UNRELIABLE, 'Unreliable'), (
            RUMOR_RELIABLE, 'Reliable'), (RUMOR_FACT, 'Fact'), (RUMOR_VAMPIRE,
                                                                'Vampire')),
        default=RUMOR_UNRELIABLE)

    def __str__(self):
        return '[{}] {} - {}: {}'.format(self.session.name, self.influence,
                                     self.rumor_type, self.description)
                                     
                                     
                                     
class InfluenceList(Model):
    character  = ForeignKey(Character, blank=True,null=True,related_name='+')
    influence1 = ForeignKey(Influence, blank=True,null=True,related_name='+')
    influence2 = ForeignKey(Influence, blank=True,null=True,related_name='+')
    influence3 = ForeignKey(Influence, blank=True,null=True,related_name='+')
    influence4 = ForeignKey(Influence, blank=True,null=True,related_name='+')
    influence5 = ForeignKey(Influence, blank=True,null=True,related_name='+')
    influence6 = ForeignKey(Influence, blank=True,null=True,related_name='+')
    
    def __str__(self): 
        return '{}: {},{},{},{},{},{}' .format (
            self.character,
            self.influence1,
            self.influence2,
            self.influence3,
            self.influence4,
            self.influence5,
            self.influence6
        )
    

