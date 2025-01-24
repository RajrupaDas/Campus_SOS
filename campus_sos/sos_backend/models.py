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

    def __str__(self):
        return f"Location of {self.user.name} at {self.timestamp}"

