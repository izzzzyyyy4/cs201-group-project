class Bike:
    def __init__(self,bike_id,bike_type):
        self.bike_id = bike_id
        self.bike_type = bike_type


    def getting_minutes(self,input_time):
        hour , minute = input_time.split(":")
        return int(hour) * 60 + int(minute)
    def drive (self,start_time,end_time):
        duration = self.getting_minutes(end_time) - self.getting_minutes(start_time)
        return duration






