from django.contrib import admin

# Register your models here.

from .models import ChargingHistory

admin.site.register(ChargingHistory)
