import uuid

from django.db import models


class UserEntity(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.TextField(null=False, max_length=32)
    last_name = models.TextField(null=False, max_length=32)
    username = models.TextField(null=False, max_length=32)
    password = models.TextField(null=False, max_length=32)

    class Meta:
        db_table = "user"
