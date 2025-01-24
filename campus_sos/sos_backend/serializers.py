# sos_backend/serializers.py
from rest_framework import serializers
from .models import User, Location

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'name', 'gender', 'custom_gender', 'year', 'user_type', 'email_verified']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['user', 'latitude', 'longitude', 'timestamp']


