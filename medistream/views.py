from rest_framework import permissions
from rest_framework import viewsets
from medistream.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class TalkViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TalkSerializer
    queryset = Talk.objects.all()


class OrganizerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrganizerSerializer
    queryset = Organizer.objects.all()