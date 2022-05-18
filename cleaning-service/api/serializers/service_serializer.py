from rest_framework import serializers
from core.models.service import Service


class  ServiceSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=60)
    cost = serializers.FloatField()
    company = serializers.CharField(max_length=30)
    #user_id = serializers.IntegerField()

    def create(self, validated_data):
        return Service.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.company = validated_data.get('company', instance.company)
        #instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.save()
        return instance 