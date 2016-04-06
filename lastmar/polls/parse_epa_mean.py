import csv
import datetime
from statistics import stdev
from math import cos, asin, sqrt

def getStateAverageData(input_file, output_file, output_file2):
	"""state_avgs is a dictionary formatted as
	'state FIPS code': [readings sum, readings count, [state readings]]
	parsed from a csv input_file. This assumes that the csv input file has the
	same format as outlined in the downloadable EPA air quality data csv files.
	"""
	state_avgs = {}
	recent_readings = {}
	with open(input_file, 'r') as csvfile:
		PM25_reader = csv.reader(csvfile, delimiter=',',
								 skipinitialspace=True)
		for reading in PM25_reader:
			key = reading[0]
			key2 = (reading[5], reading[6])
			try:
				val = float(reading[16])
				if key not in state_avgs:
					state_avgs[key] = [reading[5], reading[6],
									   val, 1, []]
				else:
					state_avgs[key][2] += val
					state_avgs[key][3] += 1
					state_avgs[key][4].append(val)
				if key2 not in recent_readings:
					recent_readings[key2] = [strToDate(reading[11]), val]
				elif strToDate(reading[11]) > recent_readings[key2][0]:
					recent_readings[key2] = [strToDate(reading[11]), val]
			except ValueError:
				pass
	"""Write state averages out to a csv file.
	Each line is 'state', 'lat', 'long',
				 'average','standard deviation',
	"""
	writer = csv.writer(open(output_file, 'w'), quotechar=' ')
	for state, data in sorted(state_avgs.items()):
		writer.writerow([state, data[0], data[1],
						data[2]/data[3], stdev(data[4])])
	"""	Writes most recent readings out to a csv file
	Each line is 'lat', 'long', 'most recent reading'.
	"""
	writer = csv.writer(open(output_file2, 'w'), quotechar=' ')
	for loc, reading in recent_readings.items():
		writer.writerow([loc[0], loc[1], reading[1]])

def strToDate(date):
	"""Format year-month-day
	"""
	return datetime.datetime.strptime(date, "%Y-%m-%d")

def HaversineDistance(lat1, lon1, lat2, lon2):
	"""Haversine formula to calculate distance adapated from:
	http://stackoverflow.com/a/21623206
	"""
	p = 0.017453292519943295
	a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) \
		* (1 - cos((lon2 - lon1) * p)) / 2
	return 12742 * asin(sqrt(a))

def mostRecentReading(lat, lon, input_file='recent_readings.csv'):
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

# getStateAverageData('daily_88502_2015.csv', 'state_avgs.csv', 'recent_readings.csv')
# print(mostRecentReading(46, -84))
# print(mostRecentReading(54, 92))
# print(mostRecentReading(6, -4))
# print(mostRecentReading(92, 45))
