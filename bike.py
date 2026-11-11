class Bike:
    standart_bike_id = []
    electric_bike_id = []

    def __init__(self,bike_id,bike_type):
        self.bike_id = bike_id
        self.bike_type = bike_type
        if self.bike_type == "standart" and self.bike_id not in Bike.standart_bike_id:
            Bike.electric_bike_id.append(self.bike_id)
        elif self.bike_type == "electric" and self.bike_id not in Bike.electric_bike_id:
            Bike.standart_bike_id.append(self.bike_id)

    def get_standart_id(self,standart_bike_id):
        return standart_bike_id
    def get_electric_id(self,electric_bike_id):
        return electric_bike_id
    def getting_minutes(self,input_time):
        hour , minute = input_time.split(":")
        return int(hour) * 60 + int(minute)
    def drive (self,start_time,end_time):
        duration = self.getting_minutes(end_time) - self.getting_minutes(start_time)
        return duration
class Standart_bike(Bike):
    def __init__(self,bike_id,bike_type = "стандартний",price_for_minute = 2):
        super().__init__(bike_id,bike_type)
        self.price_for_minute = price_for_minute
class Electric_bike(Bike):
    def __init__(self,bike_id,bike_type = "електронний",price_for_minute = 5):
        super().__init__(bike_id,bike_type)
        self.price_for_minute = price_for_minute




