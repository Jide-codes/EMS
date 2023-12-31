from django.shortcuts import render, get_object_or_404
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView

from .models import Event, Attendee
from .serializers import EventSerializer, AttendeeSerializer

class ListEventView(APIView):
    queryset = Event.objects.all()
    
    def get(self, request):
        serializer = EventSerializer(self.queryset.all(), many=True)
        return Response(serializer.data)
    
class EventDetailsView(APIView):
    
    def get(self, request, pk, format=None):
        
        event = get_object_or_404(Event, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)



class EventViewSet(viewsets.ViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        print(request.user)
        
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        event = get_object_or_404(Event, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    
    
    def update(self, request, pk=None):
        event = get_object_or_404(Event, pk=pk)
        
        if request.user != event.created_by:
            raise Response({'detail': 'You do not have permission to perform this action!'})
        
        seriliazer = EventSerializer(event, data=request.data, partial=True)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response(seriliazer.data, status=status.HTTP_200_OK)
        return Response(seriliazer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def destroy(self, request, pk=None):
        event = get_object_or_404(Event, pk=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class RegistrationView(APIView):
    
    def post(self, *args, **kwargs):
        serializer = AttendeeSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AttendeesViewSet(viewsets.ViewSet):
    queryset = Attendee.objects.all()
    permission_classes = [permissions.IsAuthenticated
                          ]
    def list(self, request):
        serializer = AttendeeSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        attendee = get_object_or_404(Attendee, pk=pk)
        serializer = AttendeeSerializer(attendee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        attendee = get_object_or_404(Attendee, pk=pk)
        serializer = AttendeeSerializer(attendee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        attendee = get_object_or_404(Attendee, pk=pk)
        attendee.delete()
        return Response({"detail":"Deleted!!!"}, status=status.HTTP_204_NO_CONTENT)