import requests
import datetime

APP_ID = "app_e072fff872cb4aee818c0fb3"
API_KEY = "nix_live_NE4J4B3ET53hZ4eJtlfgDpWqsOSZ9xvg"
SHEETY_KEY = "nix_live_NE4J4B3ET53hZ4eJtlfgDpWqsOSZ9xvg"

#x-app-id: app_e072fff872cb4aee818c0fb3
#x-app-key: nix_live_NE4J4B3ET53hZ4eJtlfgDpWqsOSZ9xvg

user_activity = input("What did you do?")



def check_calories(user_activity):
    url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
    }
    data = {
        "query": user_activity,
    }
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()

    return (response.json())

def upload_to_sheet(my_data):
    my_now = datetime.datetime.now()
    url = "https://api.sheety.co/b05b05840da8549fdb35022b7485695a/pythonMyWorkouts/workouts"
    headers = {
        "authorization": f"Bearer {SHEETY_KEY}",
    }
    data= {
        "workout" : {
            "date" : my_now.strftime("%x"),
            "time" : my_now.strftime("%X"),
            "exercise" : my_data["exercises"][0]["name"].title(),
            "duration" : my_data["exercises"][0]["duration_min"],
            "calories" : my_data["exercises"][0]["nf_calories"],
            }
        }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()



my_data = check_calories(user_activity)

print(my_data)

print(my_data["exercises"][0]["duration_min"])
upload_to_sheet(my_data)
