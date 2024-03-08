class FlightData:

    def __init__(self, nest_list: list, location: str, to_city: list):
        self.msg = ""
        for i in range(len(nest_list)):
            price, departure_time, arrive_time, fly_from, fly_to, destination_iata = nest_list[i]
            for city in to_city:

                if city[1] == destination_iata:

                    to_name = city[0]
                    part_msg = f"Low price alert! Only €{price} to fly\n{location}-{fly_from} to {to_name}-{fly_to}, from\n" \
                          f"{departure_time.split('T')[0]}—{':'.join(departure_time.split('T')[1].split(':')[:2])}" \
                               f" to {arrive_time.split('T')[0]}—{':'.join(arrive_time.split('T')[1].split(':')[:2])}."
                    self.msg += "\n" + part_msg + "\n"
        if self.msg:
            self.str()

    def str(self):
        return self.msg