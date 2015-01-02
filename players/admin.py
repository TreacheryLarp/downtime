from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from players.models import *

# Admin interface
admin.site.register(Character, SimpleHistoryAdmin)
admin.site.register(Discipline, SimpleHistoryAdmin)
admin.site.register(Title, SimpleHistoryAdmin)
admin.site.register(Age, SimpleHistoryAdmin)
admin.site.register(ActionType, SimpleHistoryAdmin)
admin.site.register(Action, SimpleHistoryAdmin)
admin.site.register(Domain, SimpleHistoryAdmin)
admin.site.register(Session, SimpleHistoryAdmin)
admin.site.register(Feeding, SimpleHistoryAdmin)
admin.site.register(ActiveDisciplines, SimpleHistoryAdmin)
admin.site.register(InfluenceRating, SimpleHistoryAdmin)
admin.site.register(Population, SimpleHistoryAdmin)
admin.site.register(Influence, SimpleHistoryAdmin)
admin.site.register(Clan, SimpleHistoryAdmin)
admin.site.register(ActionOption, SimpleHistoryAdmin)
admin.site.register(ExtraAction, SimpleHistoryAdmin)
