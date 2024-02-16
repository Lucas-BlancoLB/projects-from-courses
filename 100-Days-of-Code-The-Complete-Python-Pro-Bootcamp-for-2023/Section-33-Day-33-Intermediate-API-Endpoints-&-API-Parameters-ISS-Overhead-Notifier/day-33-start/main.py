import os
import ast
from dotenv import load_dotenv
import requests
import datetime as dt


# with requests.get(url="http://api.open-notify.org/iss-now.json") as response:
#     response.raise_for_status()
#     data = response.json()
#     print(data)  # json data
#
# iss_position = (data["iss_position"]["latitude"], data["iss_position"]["longitude"])
#
# print(iss_position)


##


load_dotenv()
info = ast.literal_eval(os.getenv("INFO"))


parameters = {
    "lat":info[0],
    "lng":info[1],
    "tzid":info[2],
    "formatted":info[3],
}

with requests.get("https://api.sunrise-sunset.org/json", params=parameters) as response_2:
    response_2.raise_for_status()
    # print(response_2.json())
    data = response_2.json()["results"]

sunrise = " ".join(data["sunrise"].split('T')[1].split(":")[:2])
sunset = " ".join(data["sunset"].split("T")[1].split(":")[:2])
print(sunrise, "sunrise", "\n" + sunset, "sunset")

hour = dt.datetime.now().hour
minute = dt.datetime.now().minute

print(hour, minute, "time")
