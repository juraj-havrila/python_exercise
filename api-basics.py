import requests
#requests.packages.urllib3.disable_warnings()
response = requests.get(url="http://api.open-notify.org/iss-now.json", verify=False)
response.raise_for_status()
print(response.status_code)
print(response.json()["iss_position"]["longitude"])

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (latitude, longitude)
print(iss_position)
