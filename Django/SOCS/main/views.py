#Imports
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	return render(request, 'main/home.html')

def about(request):
		return render(request, 'main/about.html')
@login_required
def data(request):
		return render(request, 'main/data.html')