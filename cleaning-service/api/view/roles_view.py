from api import serializers
from rest_framework import generics, viewsets

from core.models import Roles
from api.serializers.roles_serializer import RolesSerializer


class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer