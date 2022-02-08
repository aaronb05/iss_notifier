
import requests
from datetime import datetime
import config
import time

while True:
    MY_LAT = 35.963001
    MY_LONG = -79.762108

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    print(iss_latitude)
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_longitude)
    lat_distance = 12.9561 - iss_latitude
    long_distance = -87.2912 - iss_longitude

    # Your position is within +5 or -5 degrees of the ISS position.
    if -5 <= lat_distance <= 5 and -5 <= long_distance <= 5:
        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }

        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
        print(f"{sunrise}, {sunset}")
        # If the ISS is close to my current position, and it is currently dark,
        # then send email to tell me to look up.
        time_now = datetime.now()
        if sunset <= time_now.hour or time_now.hour <= sunrise:
            body = f"The Internation space station is currently at {iss_latitude}, {iss_longitude} which is within " \
                   f"{lat_distance} and {long_distance} of your location. It also currently dark enough for you to see it" \
                   f"so LOOK UP!"
            config.send_email()
    else:
        print("ISS not within view")
# BONUS: run the code every 60 seconds.
    time.sleep(60)





