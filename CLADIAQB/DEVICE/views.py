# devices/views.py
from rest_framework import viewsets
from .models import Device, SensorData
from .serializers import DeviceSerializer, SensorDataSerializer
from .permissions import IsUserOrESP32
from rest_framework.response import Response
from rest_framework import status
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsUserOrESP32]  # Adjust permissions as needed


class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    permission_classes = [IsUserOrESP32]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Send the sensor data to the WebSocket group
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "sensor_data_group",
            {
                "type": "send_sensor_data",
                "sensor_data": serializer.data,
            }
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)