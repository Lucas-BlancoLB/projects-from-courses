import os
import dotenv
import requests
import datetime as dt


dotenv.load_dotenv()
APPLICATION_ID = os.getenv("application_id")
API_KEY = os.getenv("API_KEY")
ENDPOINT = "/v2/natural/exercise"
URL = f"https://trackapi.nutritionix.com{ENDPOINT}"
URL_sheety = os.getenv("URL_SHEETY")


query = input("Enter your workout. Examples:\n-ran 3 miles\n-30 min weight lifting\n-30 min yoga\n")
# weight = int(input("How much do weight: ")) # or set a value
# height = float(input("How tall are you: ")) # or set a value
# age = int(input("How old are you: ")) # or set a value


headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": API_KEY,
}


# Parameters QUERY, WEIGHT, HEIGHT, AGE
params = {
    "query": query,
    # "weight_kg": weight,
    # "height_cm": height,
    # "age": age,
}

sheety_headers = {
    "Authorization": os.getenv("AUTHORIZATION")
}


r = requests.post(url=URL,json=params, headers=headers)
print(r.raise_for_status())
data = r.json()["exercises"]
print(data)


r_2 = requests.get(URL_sheety, headers=sheety_headers)
last_id = r_2.json()["workouts"][-1]["id"]

print(type(last_id))
now = dt.datetime.now()


nest_data = [{"workout":{"id": f"{last_id + 1 + i}",
         "date": now.strftime("%d/%m/%Y"),
         "time": now.strftime("%H:%M:%S"),
         "exercise": x["name"],
         "duration": x["duration_min"],
         "calories": x["nf_calories"]}}
        for i, x in enumerate(data)]
print(data)

for data in nest_data:
    r_2 = requests.post(URL_sheety, json=data, headers=sheety_headers)
    print(r_2.text)

