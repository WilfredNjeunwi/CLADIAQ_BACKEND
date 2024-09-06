# devices/views.py
from rest_framework import viewsets
from .models import Device, SensorData
from .serializers import DeviceSerializer, SensorDataSerializer
from .permissions import IsUserOrESP32

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsUserOrESP32]  # Adjust permissions as needed

class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    permission_classes = [IsUserOrESP32]  # Use the same permission class