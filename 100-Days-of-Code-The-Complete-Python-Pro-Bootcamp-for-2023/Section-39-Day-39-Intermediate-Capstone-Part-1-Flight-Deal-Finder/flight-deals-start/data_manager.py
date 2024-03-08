import requests


def organize_list(reference_list, nest_list):
    nested_dict = {city[0]:city[1] for city in nest_list}
    return [[city, nested_dict[city]] for city in reference_list]  # returns city_code sort by city(nam) order


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, token, URL):
        self.h = {"Authorization": token}
        self.URL = URL
        self.data = {}

        self.get_table()
        self.list_of_cities = [x["city"] for x in self.data["prices"]]



    def cheking_for_IATA_code(self, nestlist_IATA):
        reset_init = False
        # cities_n_iata = organize_list(self.list_of_cities,nestlist_IATA)
        for i in range(len(self.data["prices"])):
            # get the index if the condition is True | enumerate to hold index and item
            indice = [index for index, city in enumerate(nestlist_IATA) if city[0] == self.data["prices"][i]["city"]]
            if indice:
                if not self.data["prices"][i]["iataCode"] == nestlist_IATA[indice[0]][1]:
                    price = {"price": {"iataCode": nestlist_IATA[indice[0]][1]}}
                    self.update_table(price, self.data["prices"][i]["id"])
                    reset_init = True
        if reset_init:
            self.get_table()



    def get_table(self):
        r = requests.get(self.URL, headers=self.h)
        self.data = r.json()


    def update_table(self, price, id):
        r = requests.put(url=f"{self.URL}/{id}", json=price, headers=self.h)
        print(r.json())