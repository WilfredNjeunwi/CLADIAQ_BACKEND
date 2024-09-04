from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields you want here
    address = models.TextField(blank=True, null=True)
    organisation = models.TextField(blank=True, null=True)
    tell_num = models.TextField(blank=True, null=True)
    profileID = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username