import requests
OWM_ENDPOINT= "https://api.openweathermap.org/data/2.5/forecast"
api_key = "xxx"
LATITUDE = "x"
LONGITUDE = "x"

weather_params = {
    "lat" : LATITUDE,
    "lon" : LONGITUDE,
    "units" : "metric",
    "appid" : api_key,
    "lang" : "en",
    "cnt" : 4,              #count of 3-hour intervals for forecast (4x3 = 12 hours)
    }

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()


for interval in weather_data["list"]:
    #print(interval["weather"][0]["main"])
    if interval["weather"][0]["id"] <= 600:
        print (f"bring an umbrela, the weather will be {interval["weather"][0]["main"]}")





###############################
OWM_ENDPOINT= "https://api.openweathermap.org/data/2.5/forecast"
api_key = "x"
LATITUDE = "x"
LONGITUDE = "x"
account_sid = "x"
auth_token = "x"






weather_params = {
    "lat" : LATITUDE,
    "lon" : LONGITUDE,
    "units" : "metric",
    "appid" : api_key,
    "lang" : "en",
    "cnt" : 4,              #count of 3-hour intervals for forecast (4x3 = 12 hours)
    }




response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_it_rain=False
for interval in weather_data["list"]:
    #print(interval["weather"][0]["main"])
    if interval["weather"][0]["id"] <= 600:
        #print (f"bring an umbrela, the weather will be {interval["weather"][0]["main"]}")
        will_it_rain=True

if will_it_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today.",
        from_="+x",
        to="+x",
    )
print(message.sid)
print(message.status)
