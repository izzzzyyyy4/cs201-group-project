class Station:

  def __init__(self, name: str, bikes: list = None):
    self.name = name
    self.bikes = list(bikes) if bikes is not None else []

  def put_bikes(self, bikes_list: list) -> None:
    self.bikes.extend(bikes_list)

  def add_bike(self, bike) -> None:
    self.bikes.append(bike)

  def take_bike(self, bike_type: int):
    for bike in self.bikes:
      if bike.bike_type == bike_type:
        self.bikes.remove(bike)
        return bike
    return None

  def get_bikes_count(self) -> int:
    return len(self.bikes)

  
