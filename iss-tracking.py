import requests
from datetime import datetime
import smtplib
MY_LAT = 45.067120
MY_LONG = 25.759050
#MY_EMAIL = "XXX"
#MY_PASSWORD = "XXX"


def iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_latitude, iss_longitude

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
time_now= datetime.now().hour

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


#print (sunrise.split("T")[1].split(":")[0], sunset.split("T")[1].split(":")[0])

if time_now <= sunrise or time_now >= sunset:
    iss_latitude, iss_longitude = iss_position()
    if abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5:
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=my_email,
                msg=f"Subject:ISS in sight!\n\nLook up ISS is there."
            )
