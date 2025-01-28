# sos_backend/serializers.py
from rest_framework import serializers
from .models import User, Location, SOSAlert, CrowdedLocation, Buddy

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'name', 'gender', 'custom_gender', 'year', 'user_type', 'email_verified']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['user', 'latitude', 'longitude', 'timestamp', 'active']

# sos_backend/serializers.py

class SOSAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = SOSAlert
        fields = ['user', 'time', 'latitude', 'longitude']

class CrowdedLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrowdedLocation  # Replace with your actual model
        fields = ['users', 'time', 'latitude', 'longitude']  # Adjust the fields accordingly       fields = '__all__'  # Adjust the fields accordingly

class BuddySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # For nested representation
    buddy = UserSerializer(read_only=True)  # For nested representation

    class Meta:
        model = Buddy
        fields = ['id', 'user', 'buddy', 'matched', 'created_at']  # Include fields from your Buddy model
        read_only_fields = ['matched', 'created_at']  # Mark fields managed by the server as read-only
