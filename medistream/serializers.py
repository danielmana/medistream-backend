from rest_framework import serializers

from medistream.models import *


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality


class CustomUserSerializer(serializers.ModelSerializer):
    speciality = SpecialitySerializer()

    class Meta:
        model = CustomUser


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker


class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer


class TalkSerializer(serializers.ModelSerializer):
    speaker = SpeakerSerializer()

    class Meta:
        model = Talk


class EventSerializer(serializers.ModelSerializer):
    organizer = OrganizerSerializer()

    class Meta:
        model = Event
