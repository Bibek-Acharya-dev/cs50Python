class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f" {self.name} is eating")
class Prey(Animal):
    def flee(self):
        print(f" {self.name} is fleeing")
class Preditor(Animal):
    def hunt(self):
        print(f" {self.name} is hunting")

class Rabbit(Prey):
    pass
class Lion(Preditor):
    pass
class Hawk(Preditor,Prey):
    pass

rabbit=Rabbit("nugs")
lion=Lion("rambo")
hawk=Hawk("duck")

hawk.flee()
hawk.eat()

