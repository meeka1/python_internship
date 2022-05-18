from rest_framework import serializers
from core.models.requestStatus import RequestStatus


class RequestStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestStatus
        fields = "__all__"