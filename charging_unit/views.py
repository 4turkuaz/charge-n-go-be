from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ChargingUnitEntity
from .serializers import ChargingUnitSerializer


class ChargingUnits(APIView):
    def get(self, request):
        all_charging_units = ChargingUnitEntity.objects.all()
        serializer = ChargingUnitSerializer(all_charging_units, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChargingUnitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
