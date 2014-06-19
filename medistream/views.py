from django.contrib.auth import get_user_model

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from medistream.serializers import *
from medistream.filters import *


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


@api_view(['POST'])
def register(request):
    valid_user_fields = [f.name for f in get_user_model()._meta.fields]
    defaults = {
        # you can define any defaults that you would like for the user, here
    }
    serialized = UserSerializer(data=request.DATA)
    if serialized.is_valid():
        user_data = {field: data for (field, data) in request.DATA.items() if field in valid_user_fields}
        user_data.update(defaults)
        user = get_user_model().objects.create_user(
            **user_data
        )
        return Response(UserSerializer(instance=user).data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class TalkViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TalkSerializer
    queryset = Talk.objects.all()
    filter_class = TalkFilter


class OrganizerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrganizerSerializer
    queryset = Organizer.objects.all()


class SpeakerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SpeakerSerializer
    queryset = Speaker.objects.all()