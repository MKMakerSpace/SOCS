from django.shortcuts import render
from django.http import HttpResponse

def asset(request):
	return render(request, 'assets/list.html')