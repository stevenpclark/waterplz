from urllib.request import urlopen
import json
import time
import os
from pprint import pprint

#GET http://api.wunderground.com/api/<key>/<features>/<settings>/q/<location>.format

env = os.environ
key = env['WATERPLZ_KEY']
location = env['WATERPLZ_LOCATION']

features = 'conditions' #multiple data features can be combined in one request
url_format_str = 'http://api.wunderground.com/api/{}/{}/q/{}.json'
url = url_format_str.format(key, features, location)

f = urlopen(url)
json_string = f.read().decode('utf-8')
f.close()
parsed_json = json.loads(json_string)
pprint(parsed_json)
#city = parsed_json['location']['city']
#state = parsed_json['location']['state']
#weather = parsed_json['current_observation']['weather']
#temperature_string = parsed_json['current_observation']['temperature_string']
#feelslike_string = parsed_json['current_observation']['feelslike_string']
#print('Weather in ' + city + ', ' + state + ': ' + weather.lower() + '. The temperature is ' + temperature_string +
        #' but it feels like ' + feelslike_string + '.')

