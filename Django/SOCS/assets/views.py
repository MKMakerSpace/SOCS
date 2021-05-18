from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def asset(request):
	return render(request, 'assets/list.html')