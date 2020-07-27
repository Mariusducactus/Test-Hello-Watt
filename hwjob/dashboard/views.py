from django.shortcuts import render
from .models import Consumption, Client

def consumption_view(request, client_id, year = 2019):
	""" Addition of the method to record the monthly consumption of a given client."""
	
	client = Client.objects.get(pk=client_id)

	months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	client_consumption = []

	for month in range(1,13):
		client_consumption.append(Consumption.objects.get(year = year, month = month, client = client_id).kwh_consumed)
	
	return render(request, 'dashboard/consumption_detail.html', {
		'labels': months,
		'data': client_consumption,
		'year': year,
		'client_id': client_id,
		})
    

def search_client_view(request):
    """
        A list of clients

        TODO client.has_elec_heating should be set
        TODO client.has_anomaly should be set
    """
    return render(request, "dashboard/search_client.html")
