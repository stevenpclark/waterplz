from urllib.request import urlopen
import json
import time
import os
import folium
from pprint import pprint

#GET http://api.wunderground.com/api/<key>/<features>/<settings>/q/<location>.format

env = os.environ
key = env['WATERPLZ_KEY']
location = env['WATERPLZ_LOCATION']

features = 'conditions/geolookup' #multiple data features can be combined in one request
url_format_str = 'http://api.wunderground.com/api/{}/{}/q/{}.json'
url = url_format_str.format(key, features, location)
print(url)

f = urlopen(url)
json_string = f.read().decode('utf-8')
f.close()
data = json.loads(json_string)
#pprint(data)

#TODO: what's the diff between current_observation's location, and the location response to geolookup
current_obs= data['current_observation']
obs_loc = current_obs['observation_location']

obs_lat = obs_loc['latitude']
obs_lon = obs_loc['longitude']

geo_data = data['location']
#pprint(geo_data)
geo_lat = geo_data['lat']
geo_lon = geo_data['lon']
print(geo_lat, geo_lon)
airport_stations = geo_data['nearby_weather_stations']['airport']['station']
personal_stations = geo_data['nearby_weather_stations']['pws']['station']

if 1:
    test_map = folium.Map(location=[obs_lat, obs_lon], zoom_start=13)
    test_map.simple_marker(location=[obs_lat, obs_lon], popup='observation')
    test_map.simple_marker(location=[geo_lat, geo_lon], popup='geolocation')
    for station in airport_stations:
        test_map.simple_marker(location=[station['lat'], station['lon']], popup=station['icao'])
    for station in personal_stations:
        test_map.simple_marker(location=[station['lat'], station['lon']], popup=station['id'])
    test_map.create_map(path='test.html')
