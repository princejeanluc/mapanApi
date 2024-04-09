from api.models import  MapanEvent
from api.serializers import OrganizerSerializer, MapanEventSerializer


class MapanEventService(object):

    @staticmethod
    def getEventsFromUser(user):
        events = MapanEvent.objects.filter(organizer=user.pk)
        print(user)
        return MapanEventSerializer(events, many=True).data