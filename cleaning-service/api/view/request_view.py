from rest_framework import viewsets

from core.models import Request
from api.serializers.request_serializer import RequestSerializer


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer