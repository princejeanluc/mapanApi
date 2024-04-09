from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics, status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.models import MapanEvent, Organizer, EventType
from api.serializers import MapanEventSerializer, OrganizerSerializer, EventTypeSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from api.services import MapanEventService


class MapanEventViewSet(viewsets.ModelViewSet):
    queryset = MapanEvent.objects.all()
    serializer_class = MapanEventSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication,JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    def get(self, request, format=None):
        queryset = MapanEvent.objects.filter(organizer=self.request.user)
        serializer = MapanEventSerializer(queryset, many=True)
        return Response(self.serializer_class(serializer.data, context={'request': request}))


    @action(methods=['delete'], detail=True, url_path='/<int:id>/')
    def delete(self, request, format=None):
        try:
            mapan_event = MapanEvent.objects.filter(id=id)
            if mapan_event and mapan_event.organizer == self.request.user:
                mapan_event.delete()
                return Response("Event deleted", status=200)
            return Response("Can't delete event : May not exist or You don't have access")
        except Exception as e:
            return Response(e.message, status=404)


class OrganizerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication,JWTAuthentication]
    permission_classes = [IsAuthenticated]


class OrganizerListAPIView(generics.ListAPIView):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication,JWTAuthentication]
    permission_classes = [IsAuthenticated]



class  EventTypeViewSet(viewsets.ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
class SignupView(generics.CreateAPIView):
    serializer_class = OrganizerSerializer
    queryset = Organizer.objects.all()
    permission_classes = [AllowAny]


class EventController():

    @staticmethod
    @csrf_exempt
    @api_view(['get'])
    def getEventFromUser(request):
        events = MapanEventService.getEventsFromUser(request.user)
        return JsonResponse(events, status=status.HTTP_200_OK, safe=False)





