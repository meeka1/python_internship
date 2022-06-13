from rest_framework import serializers
from core.models.order import Order

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"