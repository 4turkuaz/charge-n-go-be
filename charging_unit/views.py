from django.db.models import F
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ChargingUnitEntity
from .serializers import ChargingUnitWriteSerializer, ChargingUnitReadSerializer


class ChargingUnits(APIView):
    def get(self, request):
        all_charging_units = ChargingUnitEntity.objects.all()
        serializer = ChargingUnitReadSerializer(all_charging_units, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChargingUnitWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChargingUnitsByUser(APIView):
    def _get_user(self, pk):
        return get_object_or_404(ChargingUnitEntity, pk=pk)

    def get(self, request, pk):
        all_charging_units = ChargingUnitEntity.objects.filter(user_id=pk)
        serializer = ChargingUnitReadSerializer(all_charging_units, many=True)
        return Response(serializer.data)


class AvailableChargingUnits(APIView):
    def get(self, request):
        all_available_charging_units = ChargingUnitEntity.objects.filter(max_slots__gt=F('occupied_slots'))
        serializer = ChargingUnitReadSerializer(all_available_charging_units, many=True)
        return Response(serializer.data)
