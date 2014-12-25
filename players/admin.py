from django.contrib import admin
from players.models import *
from reversion.helpers import patch_admin

# Admin interface
admin.site.register(Character)
admin.site.register(Discipline)
admin.site.register(Title)
admin.site.register(Boon)
admin.site.register(Debt)
admin.site.register(Age)
admin.site.register(ActionType)
admin.site.register(Action)
admin.site.register(Domain)
admin.site.register(Session)
admin.site.register(Feeding)
admin.site.register(ActiveDisciplines)
admin.site.register(InfluenceRating)
admin.site.register(Population)
admin.site.register(Influence)
admin.site.register(Clan)
admin.site.register(ActionOption)

# reversion
patch_admin(Character)
