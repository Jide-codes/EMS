from rest_framework import serializers
from .models import Event 
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
        