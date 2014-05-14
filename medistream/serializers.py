from medistream.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker


class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer


class EventSerializer(serializers.ModelSerializer):
    organizer = OrganizerSerializer()

    class Meta:
        model = Event