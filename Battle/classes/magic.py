import random

class spell:
    def __init__(self,name,cost,dmg,type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type
    def generate_dmg(self):
        dmgl = self.dmg-15
        dmgh = self.dmg+15
        return random.randrange(dmgl,dmgh)
