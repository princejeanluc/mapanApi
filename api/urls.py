from django.urls import path, include,re_path
from rest_framework import routers
from api import views
from dj_rest_auth.registration.views import VerifyEmailView



router = routers.DefaultRouter()
router.register(r'mapanevents', views.MapanEventViewSet)
router.register(r'eventtypes', views.EventTypeViewSet)



urlpatterns = [
    path('events/getEventFromUser/', views.EventController.getEventFromUser, name='getEventFromUser'),
    path('', include(router.urls), name='api'),
    path('organizer/',views.OrganizerListAPIView().as_view(),name='organizer-list'),
    path('organizer/<int:pk>/',views.OrganizerRetrieveUpdateDestroyAPIView().as_view(),name='organizer-detail'),
    path('signup/',views.SignupView().as_view(),name='signup'),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/account-confirm-email/<str:key>/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]