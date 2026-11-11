class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount):
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False