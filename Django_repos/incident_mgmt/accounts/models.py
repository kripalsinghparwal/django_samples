from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=15)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
