from django.contrib import admin

from .models import User, Location  # Import your models

admin.site.register(User)  # Register User model
admin.site.register(Location)  # Register Location model

