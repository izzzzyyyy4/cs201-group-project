class Station:
  def __init__(self, name: str, location: str):
    self.name = name
    self.location = location
    self.bikes = []
    
  def add_bike(self, bike) -> None:
     self.bikes.append(bike)
    
  def take_bike(self, bike_id: int):
     for bike in self.bikes:
            if bike.id == bike_id:
                self.bikes.remove(bike)
                return bike
        return None
    
  def get_bikes_count(self) -> int:
    return len(self.bikes)
    
  
