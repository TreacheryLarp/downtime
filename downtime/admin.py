from django.contrib import admin
from downtime.models import *
from reversion.helpers import patch_admin

# Admin interface
admin.site.register(Character)
admin.site.register(Discipline)
admin.site.register(Title)
admin.site.register(Ability)
admin.site.register(Boon)
admin.site.register(Debt)
admin.site.register(Age)
admin.site.register(ActionType)
admin.site.register(Action)
admin.site.register(Domain)
admin.site.register(Session)


# reversion
patch_admin(Character)
