# weather2mackerel
  
  Get weather data from [OpenWeatherMap](https://openweathermap.org/) and send them to [Mackerel](https://mackerel.io/ja/).

## Requirements

  Export your OpenWeatherMap API key, city ID and Mackerel API key as below:

  ```Shell
  #!/bin/bash

  export WEATHER_API_KEY='xxxxxxx'
  export WEATHER_CITY_ID='0000000'
  export MACKEREL_API_KEY='xxxxxx'
  ```

  You might also need to install 'requests':

  ```Shell
  pip3 install requests
  ```

## Usage

  ```Shell
  python3 weather2mackerel.py
  ```

## License

  MIT License
