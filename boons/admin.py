from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from boons.models import *

admin.site.register(BoonSize, SimpleHistoryAdmin)
admin.site.register(Boon, SimpleHistoryAdmin)
