from api import serializers
from rest_framework import generics, viewsets

from core.models import RequestStatus
from api.serializers.requestStatus_serializer import RequestStatusSerializer


class RequestStatusViewSet(viewsets.ModelViewSet):
    queryset = RequestStatus.objects.all()
    serializer_class = RequestStatusSerializer