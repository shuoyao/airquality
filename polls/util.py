import csv
import urllib2
import json
from math import cos, asin, sqrt

def mostRecentReading(lat, lon, input_file='station_avgs.csv'):
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
   