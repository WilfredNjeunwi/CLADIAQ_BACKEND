from django.contrib.auth.models import AbstractUser
from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=25)
    created_at = models.Date.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    # Add any additional fields you want here
    address = models.TextField(blank=True, null=True)
    organisation = models.TextField(blank=True, null=True)
    tell_num = models.TextField(blank=True, null=True)
    profileID = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username
    
class UserOrganizationRole(models.Model):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('org_user', 'Organization User')
    )
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    class Meta:
        unique_together = ('user', 'organization')