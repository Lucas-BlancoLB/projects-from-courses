import os
import dotenv
import requests

dotenv.load_dotenv()


class DataManager:
    PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_URL")
    USERS_ENDPOINT = os.getenv("SHEETY_USERS_URL")

    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.PRICES_ENDPOINT)
        self.destination_data = response.json().get("prices", {})
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city.get("iataCode")}}
            response = requests.put(
                url=f"{self.PRICES_ENDPOINT}/{city.get('id')}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=self.USERS_ENDPOINT)
        self.customer_data = response.json().get("users", {})
        return self.customer_data
