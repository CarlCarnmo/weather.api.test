import requests
import json
from typing import List
from data_class import *


#response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=58&lon=16&appid=830bd06dee61e7801c474c5b8b96b27d")

def get_weather(x,y):
    default_value = "N/A"
    api_key = "830bd06dee61e7801c474c5b8b96b27d"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={x}&lon={y}&appid={api_key}&units=metric"
    # Load the JSON data(hopefully)
    data = requests.get(url).json()

    #JSON POS Parser
    # Create the Clouds object
    clouds_data = data.get('clouds', None)
    if clouds_data:
        clouds = Clouds(clouds_data.get('all', None))
    else:
        clouds = None

    # Create the Coord object
    coord_data = data.get('coord', None)
    if coord_data:
        coord = Coord(coord_data['lon'], coord_data['lat'])
    else:
        coord = None

    # Create the Main object
    main_data = data.get('main', None)
    if main_data:
        main = Main(main_data.get('temp', None), main_data.get('feels_like', None), main_data.get('temp_min', None), main_data.get('temp_max', None), main_data.get('pressure', None), main_data.get('humidity', None), main_data.get('sea_level', None), main_data.get('grnd_level', None))
    else:
        main = None

    # Create the Snow object
    snow_data = data.get('snow', None)
    if snow_data:
        snow = Snow(snow_data.get('1h', 0))
    else:
        snow = None

    # Create the Sys object

    sys_data = data.get('sys', None)
    if sys_data:
        sys = Sys(sys_data.get('type', None), sys_data.get('id', None), sys_data.get('country', None), sys_data.get('sunrise', None), sys_data.get('sunset', None))
    else:
        sys = None


# Create the Weather objects
    weather_data = data.get('weather', None)
    if weather_data:
        weather = []
        for item in weather_data:
            weather.append(Weather(item.get('id', None), item.get('main', None), item.get('description', None), item.get('icon', None)))
    else:
        weather = None

    # Create the Wind object
    wind_data = data.get('wind', None)
    if wind_data:
        wind = Wind(wind_data.get('speed', None), wind_data.get('deg', None), wind_data.get('gust', None))
    else:
        wind = None

    # Create the Welcome10 object
    welcome10 = Welcome10(
    coord,
    weather,
    data.get('base', None),
    main,
    data.get('visibility', None),
    wind,
    snow,
    clouds,
    data.get('dt', None),
    sys,
    data.get('timezone', None),
    data.get('id', None),
    data.get('name', None),
    data.get('cod', None)
)

    print(f"{repr(welcome10)}")

#testing
#get_weather(58.32,15.12)