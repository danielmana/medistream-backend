from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import ugettext_lazy as _

from medistream.models import *


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (_('Custom fields'), {'fields': ('speciality',)}),
    )


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


class SpecialityAdmin(admin.ModelAdmin):
    pass


''' Register Admin layouts into django'''
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Organizer, OrganizerAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk, TalkAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Speciality, SpecialityAdmin)
