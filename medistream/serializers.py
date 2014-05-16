from medistream.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


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