from django.shortcuts import render
from rest_framework import viewsets

from api.models import MapanEvent, Organizer, EventType
from api.serializers import MapanEventSerializer, OrganizerSerializer, EventTypeSerializer


class MapanEventViewSet(viewsets.ModelViewSet):
    queryset = MapanEvent.objects.all()
    serializer_class = MapanEventSerializer


class OrganizerViewSet(viewsets.ModelViewSet):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer


class  EventTypeViewSet(viewsets.ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
