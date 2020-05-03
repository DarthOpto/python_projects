class Tank(object):
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.ammo = 5
        self.armor = 60

    def __str__(self):
        if self.alive:
            return "{0} ({1} armor, {2} shells)".format(self.name,
                                                        self.armor,
                                                        self.ammo)
        else:
            return "{0} (DEAD)".format(self.name)

    def fire_at(self, enemy):
        if self.ammo >= 1:
            self.ammo -= 1
            print("{0} fires on {1}".format(self.name, enemy.name))
            enemy.hit()
        else:
            print("{0} has no shells!".format(self.name))

    def hit(self):
        self.armor -= 20
        print("{0}is hit".format(self.name))
        if self.armor <= 0:
            self.explode()

    def explode(self):
        self.alive = False
        print("{0} explodes".format(self.name))
