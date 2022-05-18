from api import serializers
from rest_framework import generics, viewsets

from core.models import Request
from api.serializers.request_serializer import RequestSerializer


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer