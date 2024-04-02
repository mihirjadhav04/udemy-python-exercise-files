import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "cb3bfd5a97b64f3ea7af1a53e5a6f472"
account_sid = "AC209f6a3929bbad64d6793634567c9aa5"
auth_token = "462bfde51c56002d984c83fb52a5c655"

parameters = {
    "lat": 16.178600,
    "lon": 81.132492,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}
response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
# print(response.json())
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
# print(weather_slice)

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) <= 700:
        # print("Bring an Umbrella.")
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient(
        proxy={"http": os.environ["http_proxy"], "https": os.environ["https_proxy"]}
    )

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today.So don't forget your umberlla.",
        from_="+18503603556",
        to="+919137739416",
    )
    print(message.status)


# print(weather_data["hourly"][0]["weather"][0]["id"])
