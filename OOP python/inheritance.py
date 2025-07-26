class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("woff!")

class Cat(Animal):
    def speak(self):
        print("meow!")

dog=Dog("Rocky")
cat=Cat("kitty")

print(f"{dog.name}, {dog.is_alive}")
dog.eat()
dog.speak()
dog.sleep()
print(f"{cat.name}, {cat.is_alive}")
cat.eat()
cat.speak()
cat.sleep()
