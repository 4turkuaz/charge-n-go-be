# Generated by Django 4.1.2 on 2022-11-19 22:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserEntity",
            fields=[
                (
                    "user_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("first_name", models.TextField(max_length=32)),
                ("last_name", models.TextField(max_length=32)),
                ("username", models.TextField(max_length=32)),
                ("password", models.TextField(max_length=32)),
            ],
            options={
                "db_table": "user",
            },
        ),
    ]
