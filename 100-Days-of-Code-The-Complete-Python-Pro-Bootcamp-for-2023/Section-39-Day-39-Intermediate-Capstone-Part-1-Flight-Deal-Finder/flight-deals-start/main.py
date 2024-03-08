import os
import dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
#This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

dotenv.load_dotenv()

data_m = DataManager(os.getenv("SHEETY_TOKEN"), os.getenv("SHEETY_URL"))


flight_search = FlightSearch(os.getenv("TEQUILA_API_KEY"), os.getenv("FROM"))


location_code = flight_search.destination(data_m.list_of_cities)
data_m.cheking_for_IATA_code(location_code)
data = data_m.data


flight_list = []
for i in range(len(data["prices"])):
    search_result = flight_search.search(data["prices"][i]["iataCode"], data["prices"][i]["lowestPrice"])
    if search_result:
        flight_list.append(search_result)


for i in range(len(flight_list)):
    fl_text = FlightData(flight_list[i], os.getenv("LOCATION"), location_code)
    NotificationManager(fl_text.msg)