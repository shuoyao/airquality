import csv
# import urllib2
import urllib
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

def getStateData(stateName, input_file='state_avgs.csv'):
    stateName = ''.join(stateName.split()).lower()
    with open(input_file, 'r') as csvfile:
        state_avgs = csv.reader(csvfile, delimiter=',',
                                 skipinitialspace=True)
        for state_reading in state_avgs:
            state = ''.join(state_reading[0].split()).lower()
            if stateName == state:
                # currently set to only return mean
                # TODO: either use STD DEV info or get rid of it
                return state_reading[1]
    return

def HaversineDistance(lat1, lon1, lat2, lon2):
    """Haversine formula to calculate distance adapated from:
    http://stackoverflow.com/a/21623206
    """
    p = 0.017453292519943295
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) \
        * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))



def zipToLatLonState(yzipcode):
    # f = urllib2.urlopen('https://maps.googleapis.com/maps/api/geocode/json?address=' + str(yzipcode))
    # j = json.loads(f.read())
    # Python 3 compatability below, and Python 2 compatability above
    f = urllib.request.urlopen('https://maps.googleapis.com/maps/api/geocode/json?address=' + str(yzipcode))
    j = json.loads(f.read().decode('utf-8'))

    yourlat = j['results'][0]['geometry']['location']['lat']
    yourlon = j['results'][0]['geometry']['location']['lng']
    state = j['results'][0]['address_components'][3]["long_name"]
    return yourlat, yourlon, getStateData(state)
