#Imports
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() 
    #emergency_Contact_Name = forms.CharField(max_length=50)
    #emergency_Contact_Phone = forms.CharField(max_length=50)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() 
 
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['emergency_Contact_Name', 'emergency_Contact_Phone', 'device_mac_addresses']