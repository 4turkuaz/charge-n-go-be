from django.db import models
from user.models import UserEntity

from .src.common.location import Location
from .src.utils import get_lat_lng_from_address


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

    @property
    def location(self) -> Location:
        return get_lat_lng_from_address(self.address)

    class Meta:
        db_table = "charging_unit"


class Reservation(models.Model):
    charging_unit_id = models.AutoField(primary_key=True, editable=False)
    user_id = models.ForeignKey(UserEntity, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
