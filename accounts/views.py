from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import User
from .serializers import UserSerializer



class TestApiViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def list(self, request):
        print(request.user)
        return Response({'detail': 'User is Authenticated'})
    
    
class SignUpViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication]
    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = "User Created Succefully!"
            data['username'] = account.username
            data['email'] = account.email
            
        else:
            data = serializer.errors
        return Response(data)
    

    # def retrieve(self, request, pk=None):
    #     item = get_object_or_404(self.queryset, pk=pk)
    #     serializer = ItemSerializer(item)
    #     return Response(serializer.data)
