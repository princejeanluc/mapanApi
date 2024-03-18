from rest_framework import serializers
from api.models import Organizer, MapanEvent, EventType
from dj_rest_auth.registration.serializers import RegisterSerializer

class OrganizerSerializer(serializers.ModelSerializer):
    events = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='mapanEvent-detail')
    class Meta:
        model = Organizer
        fields = ['id', 'username','password','first_name','last_name','email','linkedin','twitter','facebook','instagram','created','updated', 'events']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return Organizer.objects.create(**validated_data)

class EventTypeSerializer(serializers.ModelSerializer):
    events = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='mapanEvent-detail')
    class Meta:
        model = EventType
        fields = ['label','events']

class MapanEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapanEvent
        fields = '__all__'

class OrganizerRegistrationSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = Organizer

    def save(self,request):
        data = self.validated_data
        data['first_name'] = self.validated_data['first_name']
        data['last_name'] = self.validated_data['last_name']
        return Organizer.objects.create(**data)