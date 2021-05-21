from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from assets.models import Asset
from django.db.models import Sum

@login_required
def asset(request):

	num_assets = Asset.objects.all().count() #Count all objects
	asset_data = Asset.objects.all()
	total_value = Asset.objects.aggregate(value=Sum('Value'))['value']
	total_purchase_value = Asset.objects.aggregate(purchaseprice=Sum('PurchasePrice'))['purchaseprice']
	title = 'Assets' #Set Page title
	
	context = { #Pass Variables into page
	'title': title,
	'num_assets': num_assets,
	'asset_data': asset_data,
	'total_value': total_value,
	'total_purchase_value': total_purchase_value
		
		}

	return render(request, 'assets/list.html', context=context)