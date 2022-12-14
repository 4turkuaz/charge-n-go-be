from django.db import models
from rest_framework import serializers

from charging_unit.models import ChargingUnitEntity


class ChargingUnitWriteSerializer(serializers.ModelSerializer):
    charging_unit_id = serializers.IntegerField(required=False)
    description = models.TextField(max_length=255, null=False)
    brand = models.TextField(max_length=32, null=False)
    model = models.TextField(max_length=32, null=False)
    address = models.TextField(max_length=128, null=False)
    occupied_slots = models.IntegerField(null=False)
    max_slots = models.IntegerField(null=False)

    class Meta:
        model = ChargingUnitEntity
        exclude = ("location",)


class ChargingUnitReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargingUnitEntity
        fields = '__all__'
