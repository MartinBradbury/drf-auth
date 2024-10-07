from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserAuth
        fields = ('email', 'username', 'id')
        
class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUserAuth
        fields = ('email', 'username', 'password1', 'password2', 'id')
        extra_kwargs = {'password' : {"write_only": True}}
        
        def validate(self, attrs):
            password = attrs.get("password1", "")
            if len(password) < 8:
                raise serializers.ValidationError("password is too short")
            if attrs['password1'] != attrs['password2']:
                raise serializers.ValidationError("Passwords do not match")
            return attrs
        
        def create(self, validated_data):
            password = validated_data.pop("password1")
            validated_data.pop("password2")
            
            return CustomUserAuth.objects.create_user(password = password, **validated_data)
        
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("incorrect credentials")
    
    
            
                    