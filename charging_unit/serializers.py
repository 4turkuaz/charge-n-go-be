from django.db import models
from rest_framework import serializers

from charging_unit.models import ChargingUnitEntity


class ChargingUnitSerializer(serializers.ModelSerializer):
    charging_unit_id = serializers.IntegerField(required=False)
    description = models.TextField(max_length=255, null=False)
    brand = models.TextField(max_length=32, null=False)
    model = models.TextField(max_length=32, null=False)
    address = models.TextField(max_length=128, null=False)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=False)
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=False)

    class Meta:
        model = ChargingUnitEntity
        fields = "__all__"
