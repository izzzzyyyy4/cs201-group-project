class Client:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
        self.bike = None

    def take_bike(self, bike):
        self.bike = bike

    def return_bike(self):
        bike = self.bike
        self.bike = None
        return bike