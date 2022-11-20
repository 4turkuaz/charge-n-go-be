import json

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from charging_unit.src.utils import get_lat_lng_from_address
from user.models import UserEntity


class ChargingUnitEntity(models.Model):
    # class Brand(models.TextChoices):
    #     TESLA = "te", _("Tesla")
    #     SHELL = "sh", _("Shell")
    #     CHARGE_POINT = "cp", _("ChargePoint")
    #     SIEMENS = "si", _("Siemens")

    charging_unit_id = models.AutoField(primary_key=True, editable=False)
    user_id = models.ForeignKey(UserEntity, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=255, null=False, default="")
    brand = models.TextField(max_length=32, null=False, default="")
    model = models.TextField(max_length=32, null=False, default="")
    address = models.TextField(max_length=128)
    occupied_slots = models.IntegerField(null=False, default=0)
    max_slots = models.IntegerField(null=False)
    location = models.TextField(blank=True, null=True, default={})

    class Meta:
        db_table = "charging_unit"


# method for updating
@receiver(post_save, sender=ChargingUnitEntity, dispatch_uid="charging_unit_id")
def update_location(sender, instance, **kwargs):
    location_dict = json.dumps(get_lat_lng_from_address(instance.address).to_json())
    instance.location = location_dict
    instance.save()


class Reservation(models.Model):
    charging_unit_id = models.AutoField(primary_key=True, editable=False)
    user_id = models.ForeignKey(UserEntity, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "reservation"
