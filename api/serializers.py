from rest_framework import serializers
from api.models import Organizer, MapanEvent, EventType
from dj_rest_auth.registration.serializers import RegisterSerializer

class OrganizerSerializer(serializers.ModelSerializer):
    mapanEvents = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='mapanEvent-detail')
    class Meta:
        model = Organizer
        fields = ['id', 'username','password','first_name','last_name','email','linkedin','twitter','facebook','instagram','created','updated', 'mapanEvents']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return Organizer.objects.create(**validated_data)

class EventTypeSerializer(serializers.ModelSerializer):
    events = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='mapanevent-detail')
    class Meta:
        model = EventType
        fields = ['pk', 'label','events']

class MapanEventSerializer(serializers.ModelSerializer):
    organizer = OrganizerSerializer(read_only=True)
    class Meta:
        model = MapanEvent
        fields = (
            'pk','title', 'description', 'date','time', 'longitude', 'latitude', 'address','image','eventType','organizer'
        )

class OrganizerRegistrationSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = Organizer


    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name')
        }
