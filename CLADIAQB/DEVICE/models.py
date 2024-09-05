from django.db import models
from USERS.models import Organization
from django.utils import timezone

# Create your models here.

class Device(models.Model):
    date_installed = models.DateTimeField(null=False, auto_created=True)
    organisation_id =models.ForeignKey(Organization, on_delete= models.CASCADE)
    location = models.CharField(max_length=255)

    def __self__(self):
        return self.organisation_id.name



class SensorData(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)
    temperature = models.IntegerField(max_length=255,null=True)
    humidity = models.IntegerField(max_length=255,null=True)
    atm_pressure = models.IntegerField(max_length=255,null=True)
    light_intensity = models.IntegerField(max_length=255,null=True)
    nh3 = models.IntegerField(max_length=255,null=True)
    co = models.IntegerField(max_length=255,null=True)
    co2 = models.IntegerField(max_length=255,null=True)
    o3 = models.IntegerField(max_length=255,null=True)
    c5h5 = models.IntegerField(max_length=255,null=True)
    cov = models.IntegerField(max_length=255,null=True)
    inflamables = models.IntegerField(max_length=255,null=True)
    picture = models.ImageField(upload_to='device_pic/', blank=True, null=True)  # Assuming picture is stored as binary data
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"SensorData from Device {self.device_id}"
    

    