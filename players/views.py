from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import models
from formtools.wizard.views import SessionWizardView
from django.utils.decorators import method_decorator
from django.forms.models import modelformset_factory
from django.contrib.auth import logout
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.core import serializers
from players import forms
from players.models import *


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
@user_passes_test(lambda u: not u.is_superuser, login_url='/gm/')
def profile(request):
    if not hasattr(request.user,'character'):
       return redirect('make character')
    session_state = []
    for session in Session.objects.order_by('name').all():
        state = session.resolved_state(request.user.character)
        session_state.append({'state': state, 'session': session})

    return render(request, 'profile.html',
                  {'character': request.user.character,
                   'session_list': session_state})

@login_required
@user_passes_test(lambda u: not u.is_superuser, login_url='/gm/')
def session(request, session):
    session = get_object_or_404(Session, pk=session)
    character = request.user.character
    data = {'session': session,
            'character': character,
            'rumor_list': Rumor.objects.filter(session=session,
                                               recipients=character),
            'submitted': character.submitted(session),
            'extra_actions': ExtraAction.objects.filter(session=session,
                                                        character=character),
            'request': request}
    return render(request, 'session.html', data)


@login_required
@user_passes_test(lambda u: not u.is_superuser, login_url='/gm/')
def wizard(request, session):
    data = {
        'user': request.user,
        'character': request.user.character,
        'session': get_object_or_404(Session,pk=session)
    }
    initial = {'0': data, '1': data, '2': data, }

    if not data['session'].is_open:
        raise PermissionDenied('Session closed')

    Action.objects.filter(character=request.user.character,
                          session=session).delete()
    ActiveDisciplines.objects.filter(character=request.user.character,
                                     session=session).delete()
    Feeding.objects.filter(character=request.user.character,
                           session=session).delete()

    session = [
            modelformset_factory(ActiveDisciplines,
                                 formset=forms.DisciplineActivationFormSet,
                                 fields=['disciplines']),
            modelformset_factory(Feeding,
                                 formset=forms.FeedingFormSet,
                                 fields=['domain', 'feeding_points',
                                         'discipline', 'description']),
            modelformset_factory(Action,
                                 formset=forms.ActionFormSet,
                                 fields=['action_type'])
        ]
        
    session1 = [
            modelformset_factory(Action,
                                 formset=forms.ActionFormSet,
                                 fields=['action_type'])
        ]
        
    return SubmitWizard.as_view(session1,
        initial_dict=initial)(request, **data)


class SubmitWizard(SessionWizardView):
    template_name = 'submit_wizard.html'

    def done(self, form_list, **kwargs):
        for f in form_list:
            f.fill_save()
        return redirect('action details', session= kwargs['session'].id)

    def get_context_data(self, form, **kwargs):
        context = super(SubmitWizard, self).get_context_data(form=form,
                                                             **kwargs)
        if self.steps.current == '0':
            context.update({'stepTitle': 'Active Disciplines'})
        elif self.steps.current == '1':
            context.update({'stepTitle': 'Feeding'})
        elif self.steps.current == '2':
            context.update({'stepTitle': 'Actions'})
            context.update({'help_texts': ActionType.help_texts()})
        return context


class ActionWizard(SessionWizardView):
    template_name = 'action_details.html'

    def done(self, form_list, **kwargs):
        for (f,action_type) in zip(form_list,kwargs['action_type']):
            print(str(action_type))
            form = f.save(commit=False)
            form.character = kwargs['character']
            form.session = kwargs['session']
            form.action_type = action_type            
            form.save()            
            serialized_obj = form.to_description()
            form.description = serialized_obj            
            form.save()
        Action.objects.filter(description="").delete()
        return redirect('session', session= kwargs['session'].id)
        
    def get_context_data(self, form, **kwargs):
        context = super(ActionWizard, self).get_context_data(form=form,**kwargs)
        action_type = form.action_type
        context.update({'stepTitle': str(action_type)})
        return context
                                                             
                                                             
@login_required
@user_passes_test(lambda u: not u.is_superuser, login_url='/gm/')
def actionDetails(request, session):
    session = get_object_or_404(Session, pk=session)
    character = request.user.character
    actions = Action.objects.filter(session=session, character=character)
    actionForms = [forms.actionToForm(action) for action in actions]
    data = {'session': session,
            'character': character,
            'action_type':[action.action_type for action in actions],
            }     
    initial = {'0': data}
    return ActionWizard.as_view(actionForms,
        initial_dict=initial)(request, **data)     



@login_required
@user_passes_test(lambda u: not u.is_superuser, login_url='/gm/')
def make_character(request):
        
    if  request.method == 'POST':
        form = forms.CharacterForm(request.POST)
        if form.is_valid(): 
            print('is valid') 
            f = form.cleaned_data           
           
            ch = Character.objects.create(
                name    = f['name'],
                age     = f['age'],
                clan    = f['clan'],
                nature  = f['nature'],
                demeanor= f['demeanor'],
                concept = f['concept'],
                   
                open_goal1  = f['open_goal1'],
                open_goal2  = f['open_goal2'],
                hidden_goal = f['hidden_goal'],
                            
                herd  = f['herd'],
                haven = f['haven'],
                    
                exp          = 0,
                humanity_exp = 0,      
                special_exp  = 0,
                
                health     = 7,
                blood      = 10,
                humanity   = f['humanity'],
                willpower  = f['willpower'],
                resources  = f['resources'],
                generation = f['generation'],
                
                additional_notes = f['additional_notes'],
                )
                
            InfluenceList.objects.create(
                character = ch,
                influence1 = f['influence_priority1'],
                influence2 = f['influence_priority2'],
                influence3 = f['influence_priority3'],
                influence4 = f['influence_priority4'],
                influence5 = f['influence_priority5'],
                influence6 = f['influence_priority6'],
                )
                
            if f['discipline1'] != None:
                dis = DisciplineRating.objects.create(
                    discipline=f['discipline1'],
                    value=f['discipline1_rating'],
                    )
                ch.disciplines.add(dis)
            
            if f['discipline2'] != None:
                dis = DisciplineRating.objects.create(
                    discipline=f['discipline2'],
                    value=f['discipline2_rating'],
                    )
                ch.disciplines.add(dis)
                
            if f['discipline3'] != None:
                dis = DisciplineRating.objects.create(
                    discipline=f['discipline3'],
                    value=f['discipline3_rating'],
                    )
                ch.disciplines.add(dis)
            
            if f['discipline4'] != None:
                dis = DisciplineRating.objects.create(
                    discipline=f['discipline4'],
                    value=f['discipline4_rating'],
                    )
                ch.disciplines.add(dis)                
                
            if f['discipline5'] != None:
                dis = DisciplineRating.objects.create(
                    discipline=f['discipline5'],
                    value=f['discipline5_rating'],
                    )
                ch.disciplines.add(dis)
            
            if f['discipline6'] != None:
                dis = DisciplineRating.objects.create(
                    discipline=f['discipline6'],
                    value=f['discipline6_rating'],
                    )
                ch.disciplines.add(dis)
            
            
            if f['hook1_name'] != "":
                hook = Hook.objects.create(
                    name=f['hook1_name'],
                    influence=f['hook1_influence'],
                    )
                for attribute in f['hook1_attributes']:
                    hook.attributes.add(attribute)    
                    hook.save()
                ch.hooks.add(hook)    
            
            if f['hook2_name'] != "":
                hook = Hook.objects.create(
                    name=f['hook2_name'],
                    influence=f['hook2_influence'],
                    )
                for attribute in f['hook2_attributes']:
                    hook.attributes.add(attribute)    
                    hook.save()
                ch.hooks.add(hook) 
                
            if f['hook3_name'] != "":
                hook = Hook.objects.create(
                    name=f['hook3_name'],
                    influence=f['hook3_influence'],
                    )
                for attribute in f['hook3_attributes']:
                    hook.attributes.add(attribute)    
                    hook.save()
                ch.hooks.add(hook)    
            
            if f['hook4_name'] != "":
                hook = Hook.objects.create(
                    name=f['hook4_name'],
                    influence=f['hook4_influence'],
                    )
                for attribute in f['hook4_attributes']:
                    hook.attributes.add(attribute)    
                    hook.save()
                ch.hooks.add(hook) 

            if f['hook5_name'] != "":
                hook = Hook.objects.create(
                    name=f['hook5_name'],
                    influence=f['hook5_influence'],
                    )
                for attribute in f['hook5_attributes']:
                    hook.attributes.add(attribute)    
                    hook.save()
                ch.hooks.add(hook)    
            
            if f['hook6_name'] != "":
                hook = Hook.objects.create(
                    name=f['hook6_name'],
                    influence=f['hook6_influence'],
                    )
                for attribute in f['hook6_attributes']:
                    hook.attributes.add(attribute)    
                    hook.save()
                ch.hooks.add(hook) 
            
            if f['equipment1_name'] != "":
                equ = Equipment.objects.create(
                    name=f['equipment1_name'],
                    influence=f['equipment1_influence'],
                    )
                ch.equipment.add(equ)
                
            if f['equipment2_name'] != "":
                equ = Equipment.objects.create(
                    name=f['equipment2_name'],
                    influence=f['equipment2_influence'],
                    )
                ch.equipment.add(equ)
                
            if f['equipment3_name'] != "":
                equ = Equipment.objects.create(
                    name=f['equipment3_name'],
                    influence=f['equipment3_influence'],
                    )
                ch.equipment.add(equ)
                
            if f['ghoul1_name'] != "":
                ghoul = Ghoul.objects.create(
                    name=f['ghoul1_name'],
                    level=f['ghoul1_level'])
                for spec in f['ghoul1_specializations']:
                    ghoul.specializations.add(spec)
                if f['ghoul1_discipline1'] != None:
                    disp_rate = DisciplineRating.objects.create(
                        discipline = f['ghoul1_discipline1'],
                        value = f['ghoul1_discipline1_rating'], 
                    )
                    ghoul.disciplines.add(disp_rate)
                if f['ghoul1_discipline2'] != None:
                    disp_rate = DisciplineRating.objects.create(
                        discipline = f['ghoul1_discipline2'],
                        value = f['ghoul1_discipline2_rating'], 
                    )
                    ghoul.disciplines.add(disp_rate)
                if f['ghoul1_discipline3'] != None:
                    disp_rate = DisciplineRating.objects.create(
                        discipline = f['ghoul1_discipline3'],
                        value = f['ghoul1_discipline3_rating'], 
                    )
                    ghoul.disciplines.add(disp_rate)
                ghoul.save()
                ch.ghouls.add(ghoul)
            
            if f['ghoul2_name'] != "":
                ghoul = Ghoul.objects.create(
                    name=f['ghoul2_name'],
                    level=f['ghoul2_level'])
                for spec in f['ghoul1_specializations']:
                    ghoul.specializations.add(spec)
                if f['ghoul2_discipline1'] != None:
                    disp_rate = DisciplineRating.objects.create(
                        discipline = f['ghoul2_discipline1'],
                        value = f['ghoul2_discipline1_rating'], 
                    )
                    ghoul.disciplines.add(disp_rate)
                if f['ghoul2_discipline2'] != None:
                    disp_rate = DisciplineRating.objects.create(
                        discipline = f['ghoul2_discipline2'],
                        value = f['ghoul2_discipline2_rating'], 
                    )
                    ghoul.disciplines.add(disp_rate)
                if f['ghoul2_discipline3'] != None:
                    disp_rate = DisciplineRating.objects.create(
                        discipline = f['ghoul2_discipline3'],
                        value = f['ghoul2_discipline3_rating'], 
                    )
                    ghoul.disciplines.add(disp_rate)
                ghoul.save()
                ch.ghouls.add(ghoul)

            if f['ghoul3_name'] != "":
                ghoul = Ghoul.objects.create(
                    name=f['ghoul3_name'],
                    level=f['ghoul3_level'])
                for spec in f['ghoul1_specializations']:
                    ghoul.specializations.add(spec)
                if f['ghoul3_discipline1'] != None:
                    disp_rate = DisciplineRating.objects.create(
                        discipline = f['ghoul3_discipline1'],
                        value = f['ghoul3_discipline1_rating'], 
                    )
                    ghoul.disciplines.add(disp_rate)
                if f['ghoul3_discipline2'] != None:
                    disp_rate = DisciplineRating.objects.create(
                        discipline = f['ghoul3_discipline2'],
                        value = f['ghoul3_discipline2_rating'], 
                    )
                    ghoul.disciplines.add(disp_rate)
                if f['ghoul3_discipline3'] != None:
                    disp_rate = DisciplineRating.objects.create(
                        discipline = f['ghoul3_discipline3'],
                        value = f['ghoul3_discipline3_rating'], 
                    )
                    ghoul.disciplines.add(disp_rate)
                ghoul.save()
                ch.ghouls.add(ghoul)
                
            soc = AttributeRating.objects.create(
                attribute =Attribute.objects.get(name='Social'),
                value= f['social_rating'],
                )
            ch.attributes.add(soc)
            
            phys = AttributeRating.objects.create(
                attribute =Attribute.objects.get(name='Physical'),
                value= f['physical_rating'],
                )
            ch.attributes.add(phys)
            
            men = AttributeRating.objects.create(
                attribute =Attribute.objects.get(name='Mental'),
                value= f['mental_rating'],
                )
            ch.attributes.add(men)
            
            for spec in f['specializations']:
                ch.specializations.add(spec)
            
            for title in f['titles']:
                ch.titles.add(title)

          #  for fact in f['canon_fact']:
          #      ch.canon_fact.add(fact)
                
            for weapon in f['weapons']:
                ch.weapons.add(weapon)
     
            ch.user = request.user   
            ch.save()   
            return redirect('profile')
        else:
           print('is not valid :(')
           print(form.errors)          
    form = forms.CharacterForm()
    
    return render(request, 'character.html', {'form': form})





        
        
