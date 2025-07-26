class Prey:
    def flee(self):
        print("this animal is fleeing")
class Preditor:
    def hunt(self):
        print("this animal is hunting")

class Rabbit(Prey):
    pass
class Lion(Preditor):
    pass
class Hawk(Preditor,Prey):
    pass

rabbit=Rabbit()
lion=Lion()
hawk=Hawk()

hawk.flee()

