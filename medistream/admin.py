from django.contrib import admin
from medistream.models import *


class EventInline(admin.TabularInline):
    model = Event


class OrganizerAdmin(admin.ModelAdmin):
    inlines = [
        EventInline,
    ]
    pass


class TalkAdmin(admin.ModelAdmin):
    pass


class TalkInline(admin.TabularInline):
    model = Talk


class SpeakerAdmin(admin.ModelAdmin):
    inlines = [
        TalkInline,
    ]
    model = Speaker


class EventAdmin(admin.ModelAdmin):
    inlines = [
        TalkInline,
    ]
    pass

''' Register Admin layouts into django'''
admin.site.register(Organizer, OrganizerAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk, TalkAdmin)