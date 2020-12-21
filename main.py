import requests
from config import API


OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

LAT = "38.432232"
LNG = "-90.378540"
weather_parameters = {
    "lat": LAT,
    "lon": LNG,
    "units": "imperial",
    "appid": API,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(OWM_endpoint, params = weather_parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]["id"]
    if int(condition_code) < 700:
        print("rain")