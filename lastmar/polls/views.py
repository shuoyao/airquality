from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from .models import mcsv
import csv
import datetime
from math import cos, asin, sqrt
from .forms import NameForm
from django.core.context_processors import csrf
from datetime import datetime
import json
import urllib2


def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def zipcode(request):
	return render(request, 'zipcode.html')

# def vote(request, question_id):
#     return HttpResponseRedirect(reverse('zipcode', args=(question_id,)))

def fillz(request):
    # if this is a POST request we need to process the form data
    args = {}
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            your_zip = request.POST.get('your_zipcode')
            your_lat,your_lon = zipToLatLon(your_zip)
            site_data = mostRecentReading(your_lat, your_lon)
        # return HttpResponseRedirect('/polls/zipcode', {'your_lat': your_lat, 'your_lon': your_lon, 'site_data': site_data})
        # return HttpResponseRedirect(reverse('zipcode',  kwargs={'your_lat': your_lat, 'your_lon': your_lon, 'site_data': site_data}))
     
        return render(request, 'zipcode.html', {'your_lat': your_lat, 'your_lon': your_lon, 'site_data': site_data})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        return render(request, 'detail.html', {'form':form })

def mostRecentReading(lat, lon, input_file='polls/recent_readings.csv'):
	"""Takes in a latitude, longitude, and input_file at returns the
	   most recent reading for the closest station.
	"""
	with open(input_file, 'r') as csvfile:
		state_avgs = csv.reader(csvfile, delimiter=',',
								 skipinitialspace=True)
		closest = 999999
		closest_reading = 0
		for reading in state_avgs:
			try:
				lat2, lon2 = float(reading[0]), float(reading[1])
				curr_dist = abs(HaversineDistance(lat, lon, lat2, lon2))
				if curr_dist < closest:
					closest = curr_dist
					closest_reading = reading[2]
			except ValueError:
				pass
		return closest_reading

def HaversineDistance(lat1, lon1, lat2, lon2):
	"""Haversine formula to calculate distance adapated from:
	http://stackoverflow.com/a/21623206
	"""
	p = 0.017453292519943295
	a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) \
		* (1 - cos((lon2 - lon1) * p)) / 2
	return 12742 * asin(sqrt(a))

def zipToLatLon(yzipcode):
    f = urllib2.urlopen('https://maps.googleapis.com/maps/api/geocode/json?address=' + str(yzipcode))
    j = json.loads(f.read())
    yourlat = j['results'][0]['geometry']['location']['lat']
    yourlon = j['results'][0]['geometry']['location']['lng']
    return yourlat, yourlon
   
    