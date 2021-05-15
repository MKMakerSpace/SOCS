#Import
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    emergency_Contact_Name = models.CharField(max_length=50, help_text="Please supply an emergency contact, this will be used in emergencies only. If you do not have an emergency contact please leave blank.", blank=True)
    emergency_Contact_Phone = models.CharField(max_length=50, blank=True)
    device_mac_addresses = models.CharField("Device MAC addresses",help_text="By adding a MAC address you are opting in to MACScanner using your device details to monitor if you are in the space. If you do not wish for this to occur please leave the space blank. Multiple addresses can be added, comma separated.",max_length=100, blank=True)
    
    def __str__(self):
        return f'{self.user.username}s Profile'
