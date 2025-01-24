from django.shortcuts import render

# Create your views here.# sos_backend/views.py
from rest_framework import viewsets
from .models import User, Location
from .serializers import UserSerializer, LocationSerializer

# User API view
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Location API view
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

