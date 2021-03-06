# Django rest
from this import d
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Own app
from ..models import SensorData
from .serializers import SensorDataSerializer


class SensorDataCreareAPIView(generics.ListCreateAPIView):
    queryset = SensorData.objects.all().order_by('-date')
    serializer_class = SensorDataSerializer
    ordering = ['-date']
    # permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)