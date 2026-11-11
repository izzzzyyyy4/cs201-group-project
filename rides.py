import client
import bike
import stations

class ManageRent:
    def __init__(self):
        self.total_revenue = 0
        self.active_rentals = {}

    def rent_bike(self, client, station, bike_id):
        bike_count = stations.get_bike_count(station)
        if bike_count <= 0:
            print("Can't rent bike")
            return
        bike = stations.take_bike(bike_id)
        if bike not in self.active_rentals:
            self.active_rentals[bike] = client


    def return_bike(self, client, bike, duration, station):
        if not self.active_rentals[bike] == client:
            print("Bike isn't yours")
            return
        if bike not in self.active_rentals:
            print("Bike not rented")
            return
        self.active_rentals.pop(bike)
        stations.add_bike(bike)



    def calculate_cost(self, bike, length):
        if bike.bike_type == "електронний":
            return length * bike.Electric_bike.price_for_minute
        if bike.bike_type == "стандартний":
            return length * bike.Standart_bike.price_for_minute

    def get_total_revenue(self):
        return self.total_revenue
