from rest_framework import viewsets, permissions
from .models import Incident
from .serializers import IncidentSerializer

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IncidentViewSet(viewsets.ModelViewSet):
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return self.request.user.incident_set.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, reporter_name=self.request.user.username)

    def perform_update(self, serializer):
        if self.get_object().status == 'Closed':
            raise PermissionDenied("Closed incidents cannot be edited.")
        serializer.save()
