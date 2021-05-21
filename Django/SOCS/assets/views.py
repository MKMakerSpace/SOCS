from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from assets.models import Asset

@login_required
def asset(request):

	num_assets = Asset.objects.all().count() #Count all objects
	asset_data = Asset.objects.all() 
	title = 'Assets' #Set Page title
	
	context = { #Pass Variables into page
		'title': title,
		'num_assets': num_assets,
		'asset_data': asset_data,
		
	}

	return render(request, 'assets/list.html', context=context)