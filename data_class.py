from typing import List


class Clouds:
    all: int

    def __init__(self, all: int) -> None:
        self.all = all
    def __repr__(self):
        return f"Clouds:\n      Clouds(%):{self.all}\n"


class Coord:
    lon: int
    lat: int

    def __init__(self, lon: int, lat: int) -> None:
        self.lon = lon
        self.lat = lat
    def __repr__(self):
        return f"Coordinates:\n      lon: {self.lon}\n      lat: {self.lat}\n"


class Main:
    temp: int
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: int
    grnd_level: int

    def __init__(self, temp: int, feels_like: float, temp_min: float, temp_max: float, pressure: int, humidity: int, sea_level: int, grnd_level: int) -> None:
        self.temp = temp
        self.feels_like = feels_like
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.pressure = pressure
        self.humidity = humidity
        self.sea_level = sea_level
        self.grnd_level = grnd_level
    def __repr__(self):
        return f"Main:\n      Temperature: {self.temp}\n      Feels like: {self.feels_like}\n      Lowest temperature: {self.temp_min}\n      Highest temperature: {self.temp_max}\n      Pressure: {self.pressure}\n      Humidity: {self.humidity}\n      Sea level: {self.sea_level}\n      Grnd level: {self.grnd_level}\n"


class Snow:
    the_1_h: float

    def __init__(self, the_1_h: float) -> None:
        self.the_1_h = the_1_h
    def __repr__(self):
        return f"\n      Snow in the last hour(mm): {self.the_1_h}"


class Sys:
    type: int
    id: int
    country: str
    sunrise: int
    sunset: int

    def __init__(self, type: int, id: int, country: str, sunrise: int, sunset: int) -> None:
        self.type = type
        self.id = id
        self.country = country
        self.sunrise = sunrise
        self.sunset = sunset
    def __repr__(self):
        return f"System:\n      type(int param): {self.type}\n      id(int param): {self.id}\n      Country: {self.country}\n      Sunrise(UTC): {self.sunrise}\n      Sunset(UTC): {self.sunset}"


class Weather:
    id: int
    main: str
    description: str
    icon: str

    def __init__(self, id: int, main: str, description: str, icon: str) -> None:
        self.id = id
        self.main = main
        self.description = description
        self.icon = icon
    def __repr__(self):
        return f"\nWeather:\n      Id: {self.id}\n      Main: {self.main}\n      Description: {self.description}\n      Icon: {self.icon}\n"


class Wind:
    speed: float
    deg: int
    gust: float

    def __init__(self, speed: float, deg: int, gust: float) -> None:
        self.speed = speed
        self.deg = deg
        self.gust = gust
    def __repr__(self):
        return f"Wind:\n      Speed: {self.speed}\n      Degrees: {self.deg}\n      Gust: {self.gust}\n"


class Welcome10:
    coord: Coord
    weather: List[Weather]
    base: str
    main: Main
    visibility: int
    wind: Wind
    snow: Snow
    clouds: Clouds
    dt: int
    sys: Sys
    timezone: int
    id: int
    name: str
    cod: int

    def __init__(self, coord: Coord, weather: List[Weather], base: str, main: Main, visibility: int, wind: Wind, snow: Snow, clouds: Clouds, dt: int, sys: Sys, timezone: int, id: int, name: str, cod: int) -> None:
        self.coord = coord
        self.weather = weather
        self.base = base
        self.main = main
        self.visibility = visibility
        self.wind = wind
        self.snow = snow
        self.clouds = clouds
        self.dt = dt
        self.sys = sys
        self.timezone = timezone
        self.id = id
        self.name = name
        self.cod = cod
    def __repr__(self) -> str:
        return f"Weather data:\n   {self.coord}\n   {self.weather}\n   {self.main}\n   Visibility(meters): {self.visibility}\n\n   {self.wind}\n   Snow: {self.snow}\n\n   {self.clouds}\n   {self.sys}\n      {self.base}\n      {self.timezone}\n      {self.id}\n      {self.dt}\n      {self.name}\n      {self.cod}"