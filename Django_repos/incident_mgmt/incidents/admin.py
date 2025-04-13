from django.contrib import admin
from .models import Incident

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('incident_id', 'user', 'incident_type', 'priority', 'status', 'reported_at')
    list_filter = ('incident_type', 'priority', 'status')
    search_fields = ('incident_id', 'reporter_name', 'user__username')
