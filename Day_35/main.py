import requests
from twilio.rest import Client
import config

account_sid = config.twilio_account_sid
auth_token = config.twilio_auth_token

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = config.OWM_api_key
parameters = {
    "lat": 41.14961,
    "lon": -8.61099,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_weather = weather_data["hourly"][:12]

will_sunny = False

for hour_data in hourly_weather:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) >= 800:
        will_sunny = True

if will_sunny:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to sunny tomorrow, ryou dont need an umbrella ☂️",
        from_='+15595464974',
        to=config.my_phone_num
    )

    print(message.status)

