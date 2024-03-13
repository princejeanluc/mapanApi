from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'organizers', views.OrganizerViewSet)
router.register(r'mapanevents', views.MapanEventViewSet)
router.register(r'eventtypes', views.EventTypeViewSet)



urlpatterns = [
    path('', include(router.urls), name='api')
]