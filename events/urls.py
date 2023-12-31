from rest_framework.routers import DefaultRouter

from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register('events', EventViewSet, basename='events')
router.register('attendees', AttendeesViewSet, basename='attendees')

urlpatterns = [
    path('', include(router.urls)),
    path('events_list/', ListEventView.as_view(), name="events_list"),
    path('event_details/<int:pk>/', EventDetailsView.as_view(), name="event_details"),
    path('event_registration/', RegistrationView.as_view(), name="event_registration")
]
 