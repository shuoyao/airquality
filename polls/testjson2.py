import json
import urllib2

def zipToLatLon(yzipcode):
    f = urllib2.urlopen('https://maps.googleapis.com/maps/api/geocode/json?address=' + str(yzipcode))
    j = json.loads(f.read())
    yourlat = j['results'][0]['geometry']['location']['lat']
    yourlon = j['results'][0]['geometry']['location']['lng']
    return yourlat, yourlon

print(zipToLatLon(94704))