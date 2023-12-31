from rest_framework import serializers
from .models import Event, Attendee
from django.contrib.auth.models import User

class EventCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class EventSerializer(serializers.ModelSerializer):
    created_by = EventCreatorSerializer(read_only=True)
    class Meta:
        model = Event
        fields = "__all__"
 
   
class SimplifiedEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title',)
             
        
class AttendeeSerializer(serializers.ModelSerializer):
    event = SimplifiedEventSerializer(read_only=True, many=True)
    class Meta:
        model = Attendee
        fields = "__all__"