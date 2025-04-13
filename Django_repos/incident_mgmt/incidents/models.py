from django.db import models
from accounts.models import User
import random
from datetime import datetime

def generate_incident_id():
    from incidents.models import Incident  # Import inside function to avoid circular import on startup

    while True:
        incident_id = f"RMG{random.randint(10000,99999)}{datetime.now().year}"
        if not Incident.objects.filter(incident_id=incident_id).exists():
            return incident_id

class Incident(models.Model):
    TYPE_CHOICES = [('Enterprise', 'Enterprise'), ('Government', 'Government')]
    PRIORITY_CHOICES = [('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')]
    STATUS_CHOICES = [('Open', 'Open'), ('In progress', 'In progress'), ('Closed', 'Closed')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    incident_id = models.CharField(max_length=20, unique=True, default=generate_incident_id, editable=False)
    incident_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    reporter_name = models.CharField(max_length=255)
    details = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.incident_id
