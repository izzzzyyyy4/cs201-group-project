import random

from client import Client
from stations import Station
from rides import ManageRent

from rides import ManageRent

def main():
    manager = ManageRent()

    stations = [Station("A"), Station("B")]
    bikes = []
    for i in range(5):
        bike = None
        bike_type = random.choice([0, 1])
        if bike_type == 0:
            bike = StandartBike(i)
        elif bike_type == 1:
            bike = ElectricBike(i)
        station = random.choice(stations)
        station.add_bike(bike)
        

    clients = [Client("Client1", 1000), Client("Client2", 500)]

    for i in range(3):
        client = random.choice(clients)
        manager.rent_bike(client, random.choice(stations))
        manager.return_bike(client, random.choice(stations))

    empty_stations = [s for s in stations if len(s.bikes) == 0]
    manager.rent_bike(client, random.choice(empty_stations))


    for client in clients:
        print(f"Client {client.name} balance:", client.balance)

    print("Total profit:", manager.get_total_revenue())
    print("Total bikes:", manager.get_total_bike_quantity())


if __name__ == "__main__":
    random.seed(1)
    main()
