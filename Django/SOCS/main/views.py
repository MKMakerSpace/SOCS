#Imports
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	return render(request, 'main/home.html')

def about(request):
	title = 'About' #Set Page title	
	context = {'title': title,}
	return render(request, 'main/about.html', context=context)

@login_required
def data(request):
	title = 'Data' #Set Page title	
	context = {'title': title,}
	return render(request, 'main/data.html', context=context)

def status(request):
	title = 'Status' #Set Page title	
	context = {'title': title,}
	return render(request, 'main/status.html', context=context)