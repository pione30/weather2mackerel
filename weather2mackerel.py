# -*- coding utf-8 -*-

import json
import os
import requests
import time

WEATHER_BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
MACKEREL_BASE_URL = 'https://api.mackerelio.com/api/v0/services/Weather/tsdb'

weather_response = requests.get(
        WEATHER_BASE_URL
        + '?id=' + os.environ['WEATHER_CITY_ID']
        + '&APPID=' + os.environ['WEATHER_API_KEY'])

headers = {
        'X-Api-Key': os.environ["MACKEREL_API_KEY"],
        'Content-Type': 'application/json'
        }

payload = [{
        'name': 'pressure',
        'time': time.time(),
        'value': weather_response.json()['main']['pressure'] - 900
        }]

mackerel_response = requests.post(
        MACKEREL_BASE_URL, headers=headers, data=json.dumps(payload))
