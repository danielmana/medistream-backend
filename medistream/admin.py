from django.contrib import admin
from medistream.models import *


class OrganizerAdmin(admin.ModelAdmin):
    pass


class TalkAdmin(admin.ModelAdmin):
    pass


class SpeakerAdmin(admin.ModelAdmin):
    pass


class TalkInline(admin.TabularInline):
    model = Talk


class EventAdmin(admin.ModelAdmin):
    inlines = [
        TalkInline,
    ]
    pass


class EventTypeAdmin(admin.ModelAdmin):
    pass

''' Register Admin layouts into django'''
admin.site.register(Organizer, OrganizerAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk, TalkAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventTypeAdmin)