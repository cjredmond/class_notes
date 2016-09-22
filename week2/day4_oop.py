class Person:
    def __init__(self, name):
        self.name = name



class Bike:
    def __init__(self, speeds, owner):
        self.speed = speeds
        self.owner = owner
        self.color = "grey"
        self._layers = 1

    def set_color(self, new_color):
        self.color = new_color
        self._layers += 1

    def display(self):
        print(self.owner.name, self.speed, self.color, self._layers)

connor = Person("Connor")
joel = Person("Joel")


bike = Bike(100, connor)
other_bike = Bike(10, joel)



bike.display()

# class Card
# Deck()
#
# for x in range(52):
#     Card().append[DECKLIST]
