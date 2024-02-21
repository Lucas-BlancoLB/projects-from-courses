import os
from dotenv import load_dotenv
import ast
import requests
import smtplib

load_dotenv()
info = ast.literal_eval(os.getenv("info"))

parameters = {
    "lat": info[0],
    "lon": info[1],
    "appid": info[2],
    "cnt": 4
}

END_POINT = "http://api.openweathermap.org/data/2.5/forecast?"

response = requests.get(END_POINT,params=parameters)
response.raise_for_status()
weather_data = response.json()["list"]

is_it_raining_today = False
for data in weather_data:

    if int(data["weather"][0]['id']) < 700:
        is_it_raining_today = True

if is_it_raining_today:
    login_info = os.getenv("login").splitlines()
    with smtplib.SMTP(login_info[0], port=587) as server:
        server.starttls()
        server.login(user=login_info[1], password=login_info[2])
        server.sendmail(from_addr=login_info[1], to_addrs=login_info[1], msg="Subject:Bring a umbrella today ☔\n\nBe ready for raining.")