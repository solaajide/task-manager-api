from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'password']
        
    
    
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise ValidationError("Username is already taken.")
        return value
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        
        user = super().create(validated_data)
        user.set_password(password)
        Token.objects.create(user=user)
        user.save()
        
        return user