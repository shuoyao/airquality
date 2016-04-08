import json
import urllib
import urllib.request

def zipToLatLon(yzipcode):
    f = urllib.request.urlopen('https://maps.googleapis.com/maps/api/geocode/json?address=' + str(yzipcode))
    j = json.loads(f)
    yourlat = j['geometry']['location']['lat']
    return yourlat

print(zipToLatLon(94704))