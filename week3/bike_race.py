class Bike:
    def __init__(self, acceleration):
        self.acceleration = acceleration
        self.location = 0


class Race:
    def __init__(self, distance):
        self.distance = distance
        self.bikes = []

    def add_bike(self, bike):
        self.bikes.append(bike)

    def add_bikes(self, bike_list):
        for bike in bike_list:
            self.add_bike(bike)

    def tick(self):
        for bike in self.bikes:
            bike.location += bike.acceleration

    def has_won(self):
        for bike in self.bikes:
            if bike.location >= self.distance:
                self.winner = bike
                return True
        return False
