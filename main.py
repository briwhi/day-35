import requests
from config import *
from twilio.rest import Client


OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"


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
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body="It's going to rain",
                from='+12518621851',
                to=phone
        )

        print(message.status)