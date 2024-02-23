import os
import dotenv
import requests
import datetime as dt
import re


def check_the_userinput(user_input):
    pattern = r"^\-?[0-9]+$"
    if re.match(pattern, user_input):
        return True


dotenv.load_dotenv()
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPHS_ENDPOINT = f"{PIXELA_ENDPOINT}/{os.getenv('login')}/graphs"
MY_ID_GRAPHS_ENDPOINT = f"{PIXELA_ENDPOINT}/{os.getenv('login')}/graphs/EDIT_ID_HERE"  # <<<<<<<<<<<<<<<<<

headers = {
    "X-USER-TOKEN": os.getenv("password")
}

params = {
    "token": os.getenv("PASSWORD"),
    "username": os.getenv("LOGIN"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

grapth_params = {
    "id": "EDIT",  # <<<<<<<<<<<<<<
    "name": "EDIT",  # <<<<<<<<<<<<<<
    "unit": 'EDIT',  # <<<<<<<<<<<<<<
    "type": "int",
    "color": "EDIT",  # <<<<<<<<<<<<<<
    "timezone": "EDIT"  # <<<<<<<<<<<<<<
}

now = dt.datetime.now()
f_now = now.strftime("%Y%m%d")

while True:
    quantity = input("type a quantity number — int:")
    if check_the_userinput(quantity):
        break

values = {
    "date": f_now,
    "quantity": quantity,
}

'''To create a user with a token'''
# r = requests.post(url=PIXELA_ENDPOINT, json=params)
# r.raise_for_status()
# print(r.text)

''''To create a graphic / related with user|token'''
# r = requests.post(url=GRAPHS_ENDPOINT,json=grapth_params, headers=headers)
# r.raise_for_status()
# print(r.text)

''''To add information in to the graphic'''
# r = requests.post(url=MY_ID_GRAPHS_ENDPOINT, json=values, headers=headers)
# r.raise_for_status()
# print(r.text)
