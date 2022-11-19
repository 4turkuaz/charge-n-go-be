import uuid


from django.db import models

from charging_unit.models import ChargingUnitEntity
from user.models import UserEntity


class Transaction(models.Model):
    transaction_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    user_id = models.ForeignKey(UserEntity, on_delete=models.CASCADE)
    charging_unit_id = models.ForeignKey(ChargingUnitEntity, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.FloatField()

    class Meta:
        db_table = "charging_history"
