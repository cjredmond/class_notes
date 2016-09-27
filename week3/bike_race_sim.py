from bike_race import Bike, Race

bike1 = Bike(4)
bike2 = Bike(7)
bike3 = Bike(8)

race = Race(50)
race.add_bikes([bike1, bike2, bike3])

while not race.has_won():
    race.tick()

print("A BIKE HAS WON! {}".format(race.winner.acceleration))
