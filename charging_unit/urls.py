from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("charging-units/", views.ChargingUnits.as_view()),
    path("charging-units/<uuid:pk>/", views.ChargingUnitsByUser.as_view()),
    path("charging-units/available/", views.AvailableChargingUnits.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
