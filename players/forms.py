from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms.models import BaseModelFormSet
from django.forms import ModelForm
from players.models import *
from django.forms import *
import django.forms

class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        super(LoginForm, self).confirm_login_allowed(user)
#        if not user.is_staff and not hasattr(user, 'character'):
#            raise forms.ValidationError(
#                "This account has no character. Please wait for a GM to add one.",
#                code='no_character', )


# Session submit forms
class SessionFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        initial = kwargs.pop('initial')
        self.user = initial['user']
        self.character = initial['character']
        self.session = initial['session']
        super(SessionFormSet, self).__init__(*args, **kwargs)

    def fill_save(self):
        self.save_existing_objects(commit=True)  # deletes objects
        instances = self.save(commit=False)
        for instance in instances:
            instance.session = self.session
            instance.character = self.character
            instance.save()
        self.save_m2m()


class DisciplineActivationFormSet(SessionFormSet):
    def __init__(self, *args, **kwargs):
        super(DisciplineActivationFormSet, self).__init__(*args, **kwargs)
        self.queryset = ActiveDisciplines.objects.filter(
            character=self.character,
            session=self.session)
        self.max_num = 1
        self.can_delete = False
        for form in self.forms:
            form.fields[
                'disciplines'].queryset = self.user.character.disciplines.all()


class ActionFormSet(SessionFormSet):
    def __init__(self, *args, **kwargs):
        super(ActionFormSet, self).__init__(*args, **kwargs)
        self.queryset = Action.objects.filter(character=self.character,
                                              session=self.session)
                                             

        self.can_delete = False

        if self.session.is_special:
            print("INITIAL")
            action_count = 2
            self.extra = action_count
            self.max_num = self.extra
            i = 0
            for action in [self.session.action_set]:
                for j in range(action.count):
                    form = self.forms[i]
                    # we could use form.initial to look at previous values. However
                    # matching the action to the option is hard.
                    form.fields['action_type'].queryset = action.action_types.all()
                    i = i + 1          

        else: 
            action_count = self.character.action_count(self.session)
            self.extra = action_count
            self.max_num = self.extra
            # otherwise django might populate the forms with actions that
            # doest match their action_type queryset
            i = 0
            for action in self.character.actions(self.session):
                for j in range(action.count):
                    form = self.forms[i]
                    # we could use form.initial to look at previous values. However
                    # matching the action to the option is hard.
                    form.fields['action_type'].queryset = action.action_types.all()
                    i = i + 1
                
class FeedingFormSet(SessionFormSet):
    def __init__(self, *args, **kwargs):
        super(FeedingFormSet, self).__init__(*args, **kwargs)
        self.queryset = Feeding.objects.filter(character=self.character,
                                               session=self.session)
        self.max_num = 3
        self.extra = 3
        self.can_delete = False
        for form in self.forms:
            form.fields[
                'discipline'].queryset = self.user.character.disciplines.all()


class CharacterForm2(ModelForm):
    class Meta:
        model = Character 
        exclude = ['user','exp','humanityExp','SpecialExp','health','blood','rituals']
       


class CharacterForm(Form):
    name = CharField(max_length=200)
    
    age     = ModelChoiceField(queryset=Age.objects,empty_label=None)
    clan    = ModelChoiceField(queryset=Clan.objects,empty_label=None)
    nature  = ModelChoiceField(queryset=Nature.objects,empty_label=None)
    demeanor= ModelChoiceField(queryset=Nature.objects,empty_label=None)

    titles = 	ModelMultipleChoiceField(queryset=Title.objects,required=False)
    
   # canon_fact        = ModelMultipleChoiceField(queryset=CanonFact.objects,required=False)
    political_faction = ModelChoiceField(queryset=PoliticalFaction.objects,empty_label=None)
    
    concept = CharField(
        widget=Textarea(attrs={'col':15,'rows':1}),
        required=False,
        )
    
    social_rating = IntegerField(initial=0)
    mental_rating = IntegerField(initial=0)
    physical_rating = IntegerField(initial=0)


    specializations = ModelMultipleChoiceField(queryset=Specialization.objects,required=False)
    
    discipline1 = ModelChoiceField(queryset=Discipline.objects,required=False)
    discipline1_rating = IntegerField(initial=0)
    discipline2 = ModelChoiceField(queryset=Discipline.objects,required=False)
    discipline2_rating = IntegerField(initial=0)
    discipline3 = ModelChoiceField(queryset=Discipline.objects,required=False)
    discipline3_rating = IntegerField(initial=0)
    discipline4 = ModelChoiceField(queryset=Discipline.objects,required=False)
    discipline4_rating = IntegerField(initial=0)
    discipline5 = ModelChoiceField(queryset=Discipline.objects,required=False)
    discipline5_rating = IntegerField(initial=0)
    discipline6 = ModelChoiceField(queryset=Discipline.objects,required=False)
    discipline6_rating = IntegerField(initial=0)

    humanity   = IntegerField(initial=7)
    willpower  = IntegerField(initial=0)
    resources  = IntegerField(initial=0)
    generation = IntegerField(initial=13) 
    
    

    
    hook1_name        = CharField(required=False)
    hook1_influence   = ModelChoiceField(queryset=Influence.objects,required=False)
    hook1_attributes  = ModelMultipleChoiceField(queryset=HookAttribute.objects,required=False)
    
    hook2_name        = CharField(required=False)
    hook2_influence   = ModelChoiceField(queryset=Influence.objects,required=False)
    hook2_attributes  = ModelMultipleChoiceField(queryset=HookAttribute.objects,required=False)
    
    hook3_name        = CharField(required=False)
    hook3_influence   = ModelChoiceField(queryset=Influence.objects,required=False)
    hook3_attributes  = ModelMultipleChoiceField(queryset=HookAttribute.objects,required=False)
    
    hook4_name        = CharField(required=False)
    hook4_influence   = ModelChoiceField(queryset=Influence.objects,required=False)
    hook4_attributes  = ModelMultipleChoiceField(queryset=HookAttribute.objects,required=False)
    
    
    hook5_name        = CharField(required=False)
    hook5_influence   = ModelChoiceField(queryset=Influence.objects,required=False)
    hook5_attributes  = ModelMultipleChoiceField(queryset=HookAttribute.objects,required=False)
    
    hook6_name        = CharField(required=False)
    hook6_influence   = ModelChoiceField(queryset=Influence.objects,required=False)
    hook6_attributes  = ModelMultipleChoiceField(queryset=HookAttribute.objects,required=False)
    
    
    influence_priority1 = ModelChoiceField(queryset=Influence.objects, label="Andrahands val för influences")
    influence_priority2 = ModelChoiceField(queryset=Influence.objects, label="Andrahands val för influences")    
    influence_priority3 = ModelChoiceField(queryset=Influence.objects, label="Andrahands val för influences")    
    influence_priority4 = ModelChoiceField(queryset=Influence.objects, label="Andrahands val för influences")
    influence_priority5 = ModelChoiceField(queryset=Influence.objects, label="Andrahands val för influences")    
    influence_priority6 = ModelChoiceField(queryset=Influence.objects, label="Andrahands val för influences")    
    

# boons
  
# relationships    
    
    open_goal1  = CharField(widget=Textarea(attrs={'col':15,'rows':3}),required=False)
    open_goal2  = CharField(widget=Textarea(attrs={'col':15,'rows':3}),required=False)
    hidden_goal = CharField(widget=Textarea(attrs={'col':15,'rows':3}),required=False)
    
    herd    = IntegerField(initial=0)
    haven   = IntegerField(initial=0)

    weapons   = ModelMultipleChoiceField(queryset=Weapon.objects,required=False)

    equipment1_name = CharField(required=False)
    equipment1_influence = ModelChoiceField(queryset=Influence.objects,required=False)
    equipment2_name = CharField(required=False)
    equipment2_influence = ModelChoiceField(queryset=Influence.objects,required=False)
    equipment3_name = CharField(required=False)
    equipment3_influence = ModelChoiceField(queryset=Influence.objects,required=False)
    
    ghoul1_name = CharField(required=False)
    ghoul1_level = IntegerField(initial=0)
    ghoul1_specializations = ModelMultipleChoiceField(queryset=Specialization.objects,required=False)
    ghoul1_discipline1 = ModelChoiceField(queryset=Discipline.objects,required=False)
    ghoul1_discipline1_rating = IntegerField(initial=0)
    ghoul1_discipline2 = ModelChoiceField(queryset=Discipline.objects,required=False)
    ghoul1_discipline2_rating = IntegerField(initial=0)
    ghoul1_discipline3 = ModelChoiceField(queryset=Discipline.objects,required=False)
    ghoul1_discipline3_rating = IntegerField(initial=0)
    
    ghoul2_name = CharField(required=False)
    ghoul2_level = IntegerField(initial=0)
    ghoul2_specializations = ModelMultipleChoiceField(queryset=Specialization.objects,required=False)
    ghoul2_discipline1 = ModelChoiceField(queryset=Discipline.objects,required=False)
    ghoul2_discipline1_rating = IntegerField(initial=0)
    ghoul2_discipline2 = ModelChoiceField(queryset=Discipline.objects,required=False)
    ghoul2_discipline2_rating = IntegerField(initial=0)
    ghoul2_discipline3 = ModelChoiceField(queryset=Discipline.objects,required=False)
    ghoul2_discipline3_rating = IntegerField(initial=0)
    
    ghoul3_name = CharField(required=False)
    ghoul3_level = IntegerField(initial=0)
    ghoul3_specializations = ModelMultipleChoiceField(queryset=Specialization.objects,required=False)
    ghoul3_discipline1 = ModelChoiceField(queryset=Discipline.objects,required=False)
    ghoul3_discipline1_rating = IntegerField(initial=0)
    ghoul3_discipline2 = ModelChoiceField(queryset=Discipline.objects,required=False)
    ghoul3_discipline2_rating = IntegerField(initial=0)
    ghoul3_discipline3 = ModelChoiceField(queryset=Discipline.objects,required=False)
    ghoul3_discipline3_rating = IntegerField(initial=0)
    
    additional_notes = CharField(widget=Textarea(attrs={'col':15,'rows':5}),required=False)




excludedFields  = ['character','action_type','session','description','resolved']

class ActionForm(ModelForm):
    class Meta:
        model = Action
        exclude = excludedFields    

    
class AidActionForm(ActionForm):
    class Meta:
        model = AidAction
        exclude = excludedFields
    action_type = "Aid Action"

class ConserveInfluenceForm(ActionForm):
    class Meta:
        model = ConserveInfluence
        exclude = excludedFields
    action_type = "Conserve (Influence)"

class ConserveDomainForm(ActionForm):
    class Meta:
        model = ConserveDomain
        exclude = excludedFields
    action_type = "Conserve (Domain)"

class InfluenceForgeForm(ActionForm):
    class Meta:
        model = InfluenceForge
        exclude = excludedFields
    action_type = "Influence (Forge)"

class InfluenceStealForm(ActionForm):
    class Meta:
        model = InfluenceSteal
        exclude = excludedFields
    action_type = "Influence (Steal)"
        
class InfluenceDestroyForm(ActionForm):
    class Meta:
        model = InfluenceDestroy
        exclude = excludedFields
    action_type = "Influence (Destroy)"

class InvestigateCharacterInfluenceForm(ActionForm):
    class Meta:
        model = InvestigateCharacterInfluence
        exclude = excludedFields
    action_type = "Investigate (Character: Influence)"

class InvestigateCharacterResourcesForm(ActionForm):
    class Meta:
        model = InvestigateCharacterResources
        exclude = excludedFields
    action_type = "Investigate (Character: Resources)"
        
class InvestigateCharacterDowntimeActionsForm(ActionForm):
    class Meta:
        model = InvestigateCharacterDowntimeActions
        exclude = excludedFields
    action_type = "Investigate (Character: Downtime Actions)"

class InvestigateCounterSpionageForm(ActionForm):
    class Meta:
        model = InvestigateCounterSpionage
        exclude = excludedFields
    action_type = "Investigate (Counter spionage)"

class InvestigatePhenomenonForm(ActionForm):
    class Meta:
        model = InvestigatePhenomenon
        exclude = excludedFields
    action_type = "Investigate (Phenomenon)"
        
class InvestigateInfluenceForm(ActionForm):
    class Meta:
        model = InvestigateInfluence
        exclude = excludedFields
    action_type = "Investigate (Influence)"

class LearnAttributeForm(ActionForm):
    class Meta:
        model = LearnAttribute
        exclude = excludedFields
    action_type = "Learn (Attribute)"

class LearnDisciplineForm(ActionForm):
    class Meta:
        model = LearnDiscipline
        exclude = excludedFields
    action_type = "Learn (Discipline)"

class LearnSpecializationForm(ActionForm):
    class Meta:
        model = LearnSpecialization
        exclude = excludedFields
    action_type = "Learn (Specialization)"




class InvestGhoulForm(ActionForm):
    class Meta:
        model = InvestGhoul
        exclude = excludedFields
    action_type = "Invest (Ghoul)"
        
class InvestEquipmentForm(ActionForm):
    class Meta:
        model = InvestEquipment
        exclude = excludedFields
    action_type = "Invest (Equipment)"

class InvestWeaponForm(ActionForm):
    class Meta:
        model = InvestWeapon
        exclude = excludedFields
    action_type = "Invest (Weapon)"

class InvestHerdForm(ActionForm):
    class Meta:
        model = InvestHerd
        exclude = excludedFields
    action_type = "Invest (Herd)"
        
class InvestHavenForm(ActionForm):
    class Meta:
        model = InvestHaven
        exclude = excludedFields
    action_type = "Invest (Haven)"

class MentorAttributeForm(ActionForm):
    class Meta:
        model = MentorAttribute
        exclude = excludedFields
    action_type = "Mentor (Attribute)"

class MentorDisciplineForm(ActionForm):
    class Meta:
        model = MentorDiscipline
        exclude = excludedFields
    action_type = "Mentor (Discipline)"
    
class MentorSpecializationForm(ActionForm):
    class Meta:
        model = MentorSpecialization
        exclude = excludedFields
    action_type = "Mentor (Specialization)"

class RestForm(ActionForm):
    class Meta:
        model = Rest
        exclude = excludedFields
    action_type = "Rest"
        
class NeglectDomainForm(ActionForm):
    class Meta:
        model = NeglectDomain
        exclude = excludedFields
    action_type = "Neglegera domän"        

class PatrolDomainForm(ActionForm):
    class Meta:
        model = PatrolDomain
        exclude = excludedFields
    action_type = "Patrullera domän"  
    
class KeepersQuestionForm(ActionForm):
    class Meta:
        model = KeepersQuestion
        exclude = excludedFields
    action_type = "Elysiemästarens fråga"  

class PrimogensQuestionForm(ActionForm):
    class Meta:
        model = PrimogensQuestion
        exclude = excludedFields
    action_type = "Primogenens fråga"  
                
class PrimogensAidActionForm(ActionForm):
    class Meta:
        model = PrimogensAidAction
        exclude = excludedFields
    action_type = "Primogenens Aid Action"  


formTable = {
    'Aid Action':AidActionForm, 
    'Conserve (Influence)':ConserveInfluenceForm,
    'Conserve (Domain)':ConserveDomainForm,
    'Influence (Forge)':InfluenceForgeForm,
    'Influence (Steal)':InfluenceStealForm,
    'Influence (Destroy)':InfluenceDestroyForm,
    'Investigate (Character: Influence)':InvestigateCharacterInfluenceForm,
    'Investigate (Character: Resources)':InvestigateCharacterResourcesForm,
    'Investigate (Character: Downtime Actions)':InvestigateCharacterDowntimeActionsForm,
    'Investigate (Counter spionage)':InvestigateCounterSpionageForm,
    'Investigate (Phenomenon)':InvestigatePhenomenonForm,
    'Investigate (Influence)':InvestigateInfluenceForm,
    'Learn (Attribute)':LearnAttributeForm,
    'Learn (Discipline)':LearnDisciplineForm,
    'Learn (Specialization)':LearnSpecializationForm,
    'Invest (Ghoul)':InvestGhoulForm,
    'Invest (Equipment)':InvestEquipmentForm,
    'Invest (Weapon)':InvestWeaponForm,
    'Invest (Herd)':InvestHerdForm,
    'Invest (Haven)':InvestHavenForm,
    'Mentor (Attribute)':MentorAttributeForm,
    'Mentor (Discipline)':MentorDisciplineForm,
    'Mentor (Specialization)':MentorSpecializationForm,
    'Rest':RestForm,
    'Neglegera domän':NeglectDomainForm,
    'Patrullera domän':PatrolDomainForm,
    'Primogenens fråga':PrimogensQuestionForm,
    'Primogenens Aid Action':PrimogensAidActionForm,
    'Elysiemästarens fråga':KeepersQuestionForm,
    
    }
                
def actionToForm(action):
    try:
        return formTable[str(action.action_type)]
    except KeyError:
        return ActionForm
    
    
    
    
                  
