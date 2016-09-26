class Monster:
    def __init__(self):
        self.hp = 10
    def dead(self):
        if self.hp <= 0:
            print("{} is dead".format(self.name))


class Weapon:
    def __init__(self):
        self.damage = 0
        self.durability = 0

    def attack(self):
        self.set_durability()
        return self.damage

    def set_durability(self):
        self.durability -= 1
        if self.durability < 0:
            self.durability = 0
            self.damage = 0

class Sword(Weapon):
    def __init__(self):
        self.damage = 3
        self.durability = 2

class UnbreakableSword(Sword):
    def set_durability(self):
        pass



orc = Monster()
bad_sword = Weapon()
ok_sword = Sword()
awesome_sword = UnbreakableSword()

orc.hp -= awesome_sword.attack()
print(orc.hp)
