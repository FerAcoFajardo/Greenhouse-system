# Django rest
from this import d
from rest_framework import generics
from rest_framework.response import Response
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
    
    
# View to get the last data from the sensor
class SensorDataLastAPIView(generics.RetrieveAPIView):
    # queryset = SensorData.objects.all().order_by('-date')
    serializer_class = SensorDataSerializer
    ordering = ['-date']
    pagination_class = None
    
    # def get_queryset(self):
    #     return SensorData.objects.filter(sensor=self.kwargs['pk']).order_by('-date')[:1]
    def get_object(self):
        data = SensorData.objects.filter(sensor=self.kwargs['pk']).order_by('-date').first()
        data = self.serializer_class(data, many=False)
        print(data)
        return data.data
    def retrieve(self, request, *args, **kwargs):
        data = self.get_object()
        return Response(data)