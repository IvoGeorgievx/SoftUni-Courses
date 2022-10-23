class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def defend(self, amount):
        if self.health - amount <= 0:
            self.health = 0
            return f"{self.name} was defeated"
        self.health -= amount

    def heal(self, amount):
        self.health += amount


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))