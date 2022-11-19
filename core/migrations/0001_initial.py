# Generated by Django 4.1.2 on 2022-11-19 23:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user", "0001_initial"),
        ("charging_unit", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "transaction_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
                ("price", models.FloatField()),
                (
                    "charging_unit_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="charging_unit.chargingunitentity",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.userentity",
                    ),
                ),
            ],
            options={
                "db_table": "charging_history",
            },
        ),
    ]
