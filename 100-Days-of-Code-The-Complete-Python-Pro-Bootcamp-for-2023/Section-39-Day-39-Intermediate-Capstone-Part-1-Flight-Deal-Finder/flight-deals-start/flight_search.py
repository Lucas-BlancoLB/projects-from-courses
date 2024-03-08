import datetime as dt
import requests
import json





class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, API_KEY, FROM):
        self.ENDPOINT_SEARCH = "https://api.tequila.kiwi.com/v2/search"
        self.ENDPOINT_DESTINATION = "https://api.tequila.kiwi.com/locations/topdestinations"
        date = dt.datetime.now()
        self.params = {
            "fly_from": FROM,  # IATA code
            "fly_to": str(),  # IATA code
            "date_from": date.strftime("%d/%m/%Y"),
            "date_to ": (date + dt.timedelta(days=30 * 6)).strftime("%d/%m/%Y"),  # CHANGE TO 30 * 6
            "price_to": int(),  # max price
            "sort": "price,date"
        }
        self.h = {"apikey": API_KEY}
        self.data = None


    def search(self, destination: str, lower_then: int):
        self.params["fly_to"] = destination
        self.params["price_to"] = lower_then
        r = requests.get(self.ENDPOINT_SEARCH, params=self.params, headers=self.h)
        self.data = r.json()
        print(json.dumps(self.data, indent=4))
        if self.data["data"]:

            return [[self.data["data"][i]["price"],
                     self.data["data"][i]["route"][0]["local_departure"],
                     self.data["data"][i]["route"][0]["local_arrival"],
                     self.data["data"][i]["flyFrom"], self.data["data"][i]["flyTo"], destination]
                    for i in range(min(len(self.data["data"]), 3))]
        else:
            return False

    def destination(self, destination_list):
        p = {"term": "london_gb"}  # using london_gb returns 100 "id"s, not only london
        r = requests.get(self.ENDPOINT_DESTINATION,params=p ,headers=self.h)
        data = r.json()
        return [[data["locations"][i]["name"],data["locations"][i]["code"]]
                for i in range(len(data["locations"]))
                if data["locations"][i]["name"] in destination_list ]
