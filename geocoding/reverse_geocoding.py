import json
import urllib
import urllib2

"""
Reverse geocoding (from lat, lon to address) using Nominatim
on Open Street Map, MapQuest, or custom API endpoints.
http://wiki.openstreetmap.org/wiki/Nominatim
"""

MAPQUEST_URL = "http://open.mapquestapi.com/nominatim/v1/reverse?"
OSM_URL = "http://nominatim.openstreetmap.org/reverse?"


class ReverseGeocoder(object):
    def __init__(self, url=MAPQUEST_URL):
        """ Set url to either OSM_URL, MAPQUEST_URL, or your own Nominatim server. """
        self.base_url = url

    def reverse_geocode(self, lat, lon):
        """ Reverse geocoding in Nominatim format. Returns dict. """        
        query = {'format':'json', 'lat':lat, 'lon':lon}
        
        url = self.base_url + urllib.urlencode(query)
        response = urllib2.urlopen(url).read()
        
        try:
            jsondata = json.loads(response)
        except:
            jsondata = {'display_name':"", 'place_id':"", 'osm_id':"", 'address':""}
        
        return jsondata
    
    def get_address(self, lat, lon):
        jsondata = self.reverse_geocode(lat, lon)
        if 'error' in jsondata:
            return jsondata
        else:
            return jsondata['address']

