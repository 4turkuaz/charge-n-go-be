from django.contrib import admin

# Register your models here.

from .models import UserEntity

admin.site.register(UserEntity)
