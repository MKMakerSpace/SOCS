#Import
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    emergency_Contact_Name = models.CharField(max_length=50)
    emergency_Contact_Phone = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.user.username}s Profile'
