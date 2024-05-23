from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец стреляет из лука."

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.weapon = weapon
            print(f"{self.name} выбирает {weapon.__class__.__name__.lower()}.")

    def attack(self):
        if self.weapon:
            print(self.weapon.attack())
        else:
            print(f"{self.name} не имеет оружия.")

class Monster:
    def __init__(self, name):
        self.name = name

    def defeat(self):
        print(f"{self.name} побежден!")


fighter = Fighter("Боец Иван")
monster = Monster("Монстр")


sword = Sword()
fighter.changeWeapon(sword)


fighter.attack()
monster.defeat()


bow = Bow()
fighter.changeWeapon(bow)


fighter.attack()
monster.defeat()