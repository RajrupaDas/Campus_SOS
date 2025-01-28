from django.shortcuts import render

# Create your views here.# sos_backend/views.py
from rest_framework import viewsets
from .models import User, Location, SOSAlert, Buddy
from .serializers import UserSerializer, LocationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User as DjangoUser
from rest_framework import generics
from .serializers import SOSAlertSerializer, CrowdedLocationSerializer, BuddySerializer
import math
from .models import CrowdedLocation

def haversine(lat1, lon1, lat2, lon2):
    # Calculate distance between two points on the Earth using Haversine formula
    radius = 6371  # Earth radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c  # Result in kilometers
    return distance

@api_view(['POST'])
def update_location(request):
    try:
        # Extract latitude and longitude from the request body
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')
        user = DjangoUser.objects.get(username=request.user.username)  # You can use any auth method here

        # Create or update the user's location
        location, created = Location.objects.update_or_create(
            user=user,
            defaults={'latitude': latitude, 'longitude': longitude, 'active': True}
        )

        return Response({"message": "Location updated successfully"}, status=status.HTTP_200_OK)
    except DjangoUser.DoesNotExist:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

# User API view
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Location API view
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        # Get the location object for the current user, or create one if it doesn't exist
        return Location.objects.get_or_create(user=self.request.user)[0]

# sos_backend/views.py

class SOSAlertView(generics.CreateAPIView):
    queryset = SOSAlert.objects.all()
    serializer_class = SOSAlertSerializer
    permission_classes = [IsAuthenticated]

class NearestCrowdedLocationView(generics.ListAPIView):
    serializer_class = CrowdedLocationSerializer

    def get_queryset(self):
        # Fetch the user’s location and calculate proximity
        user_location = self.request.user.userlocation
        user_lat, user_lon = user_location.latitude, user_location.longitude

        crowded_locations = CrowdedLocation.objects.all()
        nearest_location = min(crowded_locations, key=lambda loc: haversine(user_lat, user_lon, loc.latitude, loc.longitude))

        return [nearest_location]

# sos_backend/views.py

class MatchBuddyView(generics.CreateAPIView):
    queryset = Buddy.objects.all()
    serializer_class = BuddySerializer

    def perform_create(self, serializer):
        user = self.request.user
        buddy_user = User.objects.get(id=self.request.data['buddy_id'])  # Assume buddy_id is provided
        
        # Match based on proximity logic
        # If they're close enough, create a match
        user_location = user.userlocation
        buddy_location = buddy_user.userlocation
        distance = haversine(user_location.latitude, user_location.longitude, buddy_location.latitude, buddy_location.longitude)
        
        if distance < 5:  # If within 5 km, match
            serializer.save(user=user, buddy=buddy_user, matched=True)

