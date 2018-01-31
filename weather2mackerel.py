# -*- coding utf-8 -*-

import json
import os
import requests
import time

WEATHER_BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
MACKEREL_BASE_URL = 'https://api.mackerelio.com/api/v0/services/Weather/tsdb'


def main():

    weather_response = requests.get(
        WEATHER_BASE_URL
        + '?id=' + os.environ['WEATHER_CITY_ID']
        + '&APPID=' + os.environ['WEATHER_API_KEY']
    )

    headers = {
        'X-Api-Key': os.environ["MACKEREL_API_KEY"],
        'Content-Type': 'application/json'
    }

    payload = []
    payload.append({
        'name': 'pressure',
        'time': time.time(),
        'value': weather_response.json()['main']['pressure'] - 900
    })
    payload.append({
        'name': 'percentage.humidity',
        'time': time.time(),
        'value': weather_response.json()['main']['humidity']
    })

    requests.post(
        MACKEREL_BASE_URL, headers=headers, data=json.dumps(payload)
    )


if __name__ == '__main__':
    main()
