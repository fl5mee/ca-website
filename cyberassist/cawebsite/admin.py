from django.contrib import admin

from .models import Event, Team, Branch

admin.site.register(Event)
admin.site.register(Team)
admin.site.register(Branch)