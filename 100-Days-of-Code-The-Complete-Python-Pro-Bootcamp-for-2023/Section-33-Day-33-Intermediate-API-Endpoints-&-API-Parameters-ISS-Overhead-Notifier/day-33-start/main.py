import requests

with requests.get(url="http://api.open-notify.org/iss-now.json") as response:
    response.raise_for_status()
    data = response.json()
    print(data)  # json data

iss_position = (data["iss_position"]["latitude"], data["iss_position"]["longitude"])

print(iss_position)
