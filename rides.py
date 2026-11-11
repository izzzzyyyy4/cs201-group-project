import client
import bike
import stations

class ManageRent:
    def __init__(self):
        self.total_revenue = 0
        self.active_rentals = {}

    def rent_bike(self, client, station):
        bike_count = stations.get_bike_count(station)
        if bike_count <= 0:
            print("Can't rent bike")
            return
        bike = stations.take_bike(bike_id)
        if bike not in self.active_rentals:
            self.active_rentals[bike] = [client]

    def return_bike(self, client, bike, duration, station):

        if bike not in self.active_rentals:
            print("Bike not rented")
            return
        self.active_rentals.pop(bike)
        stations.add_bike(bike)



    def calculate_cost(self, bike, length):
        # check if bike is electric or normal, calculate cost accordingly
        # electric - 5uah/hr; normal - 2uah/hr
        if bike.bike_type == "електронний":
            self.total_revenue += length * bike.Electric_bike.price_for_minute
        if bike.bike_type == "стандартний":
            self.total_revenue += length * bike.Standart_bike.price_for_minute

    def get_total_revenue(self):
        return self.total_revenue
