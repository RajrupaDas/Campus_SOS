from django.db import models

# Model to store User information
class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user_id = models.CharField(max_length=100, unique=True)  # Use campus email ID as unique identifier
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    custom_gender = models.CharField(max_length=100, blank=True, null=True)  # Allow users to define a custom gender
    year = models.CharField(max_length=50)  # Campus year or staff designation
    user_type = models.CharField(max_length=50, choices=[('student', 'Student'), ('staff', 'Staff'), ('security', 'Security')])  # Student, Staff, or Security
    email_verified = models.BooleanField(default=False)  # Whether the user has been verified

    def __str__(self):
        return self.name

# Model to store Location data
class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link the location to a user
    latitude = models.FloatField()  # Store latitude as a float
    longitude = models.FloatField()  # Store longitude as a float
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp for when the location was recorded
    active = models.BooleanField(default=True)  # Whether the user is active (visible on the map)

    def __str__(self):
        return f"Location of {self.user.name} at {self.timestamp}"

# sos_backend/models.py

class SOSAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who triggered the SOS
    time = models.DateTimeField(auto_now_add=True)  # Time of alert
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def __str__(self):
        return f"SOS Alert from {self.user.username} at {self.time}"

# sos_baceend/models.py

class CrowdedLocation(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def __str__(self):
        return self.name

class Buddy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buddy = models.ForeignKey(User, related_name='buddies', on_delete=models.CASCADE)
    matched = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.buddy.username} (Matched: {self.matched})"
