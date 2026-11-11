from client import Client
from bike import Bike
from stations import Station

class ManageRent:
    def __init__(self):
        self.total_revenue = 0
        self.active_rentals = {}

    def rent_bike(self, client, bike_id):
        bike_count = Station.get_bike_count()
        if bike_count <= 0:
            print("Can't rent bike")
            return
        bike = Station.take_bike(bike_id)
        if bike not in self.active_rentals:
            self.active_rentals[bike] = client


    def return_bike(self, client, bike, duration):
        if not self.active_rentals[bike] == client:
            print("Bike isn't yours")
            return
        if bike not in self.active_rentals:
            print("Bike not rented")
            return
        self.active_rentals.pop(bike)
        Station.add_bike(bike)
        cost = self.calculate_cost(bike, duration)
        self.total_revenue += cost
        Client.pay(cost)



    def calculate_cost(self, bike, length):
        if Bike.bike_type == "electric":
            return length * bike.Electric_bike.price_for_minute
        if Bike.bike_type == "standart":
            return length * bike.Standart_bike.price_for_minute

    def get_total_revenue(self):
        return self.total_revenue
