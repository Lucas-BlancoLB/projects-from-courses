import os
from dotenv import load_dotenv
import ast
import requests
from datetime import datetime
import config
import time


load_dotenv()

MY_LAT, MY_LONG  = ast.literal_eval(os.getenv("info"))
login = os.getenv("login").splitlines()

is_iss_close_by = False

while not is_iss_close_by:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat_n_lng= [float(data["iss_position"]["latitude"]), float(data["iss_position"]["longitude"])]
    # iss_lat_n_lng = [MY_LAT-5, MY_LONG+5]
    # print(iss_lat_n_lng)


    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid":'America/Sao_Paulo'
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_n_sunset = [int(data["results"]["sunrise"].split("T")[1].split(":")[0]),
                        int(data["results"]["sunset"].split("T")[1].split(":")[0])]


    time_now = int(str(datetime.now()).split()[1].split(":")[0])

    looking_for_iss = config.IsISSClose(parameters, iss_lat_n_lng, sunrise_n_sunset, time_now, login)


    var = looking_for_iss.is_iSS_close()
    if var:
        is_iss_close_by = True
        print("LOOK UP")
    else:
        print(f"ISS LOCATION: lat {iss_lat_n_lng[0]} & lng {iss_lat_n_lng[1]}\nmy location: lat {MY_LAT} & lng {MY_LONG}\n")
        time.sleep(60)
