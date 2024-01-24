from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+91\d{10}$', message="Phone number must start with +91 and have a total of 12 digits.")
    phone = models.CharField(max_length=15, null=True, blank=True)
