from django.contrib.auth.models import User
from rest_framework.validators import ValidationError
from rest_framework import serializers
import re


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    confirm_password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only':True}}
        
    def validate_password(self, value):
        if len(value) < 6:
            raise ValidationError("Password must be at least 6 character long")
        if not re.search(r'[A-Z]', value):
            raise ValidationError("Password must contain at least one uppercase letter")
        if not re.search(r'[a-z]', value):
            raise ValidationError("Password must contain at least one lowercase letter")
        if not re.search(r'[0-9!@#$%^&*()_+=-]', value):
            raise ValidationError("Password must contain ar least on number or symbol")
        return value
        
        
    def save(self):
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        
        if password != confirm_password:
            raise ValidationError({'Error': 'Password should be the same as confirm password'})
        if User.objects.filter(email=self.validated_data['email'],).exists():
            raise ValidationError({'Error': 'Email already exists!'})
        
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account
        