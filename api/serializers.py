
from rest_framework import serializers

from api.models import Organizer, MapanEvent, EventType


class OrganizerSerializer(serializers.ModelSerializer):
    events = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='mapanEvent-detail')
    class Meta:
        model = Organizer
        fields = '__all__'

class EventTypeSerializer(serializers.ModelSerializer):
    events = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='mapanEvent-detail')
    class Meta:
        model = EventType
        fields = ['label','events']

class MapanEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapanEvent
        fields = '__all__'




