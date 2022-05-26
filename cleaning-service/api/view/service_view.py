from rest_framework import viewsets

from core.models import Service
from api.serializers.service_serializer import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer