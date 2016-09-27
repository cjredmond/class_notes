from bike_race import Bike, Race
def test_can_create_bike():
    bike = Bike(5)
    assert bike.acceleration == 5
    assert bike.location == 0

def test_can_create_race():
    race = Race(300)
    assert race.distance == 300

def test_can_add_bike_to_race():
    race = Race(300)
    bike = Bike(1)
    race.add_bike(bike)
    assert race.bikes == [bike]


def test_can_add_bikes_to_race():
    race = Race(300)
    bike1 = Bike(1)
    bike2 = Bike(1)
    bike3 = Bike(1)
    race.add_bikes([bike1, bike2, bike3])
    assert race.bikes == [bike1, bike2, bike3]

def test_can_tick_all_bikes_forward():
    race = Race(300)
    bike1 = Bike(4)
    bike2 = Bike(2)
    bike3 = Bike(10)
    race.add_bikes([bike1, bike2, bike3])
    race.tick()
    assert race.bikes[0].location == 4
    assert race.bikes[1].location == 2
    assert race.bikes[2].location == 10

def test_can_notify_if_bike_has_won():
    race = Race(4)
    bike = Bike(1)
    race.add_bike(bike)
    race.tick()
    race.tick()
    race.tick()
    race.tick()
    assert race.has_won() == True

def test_will_tell_you_who_won():
    race = Race(4)
    bike1 = Bike(1)
    bike2 = Bike(2)
    bike3 = Bike(1)
    race.add_bikes([bike1,bike2,bike3])
    race.tick()
    race.tick()
    race.has_won()
    assert race.winner == bike2

def test_will_tell_winner_correctly_if_they_are_passed_finish():
    race = Race(50)
    bike1 = Bike(4)
    bike2 = Bike(7)
    bike3 = Bike(5)
    race.add_bikes([bike1,bike2,bike3])
    while not race.has_won():
        race.tick()

    assert race.winner == bike2
