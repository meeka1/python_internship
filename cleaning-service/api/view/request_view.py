from rest_framework import viewsets

from core.models import Order
from api.serializers.request_serializer import RequestSerializer


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = RequestSerializer