import django_filters
from medistream.models import Talk


class TalkFilter(django_filters.FilterSet):

    class Meta:
        model = Talk
        fields = ['event']