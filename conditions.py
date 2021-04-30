class Point:
    def __init__(self, x, y): # constructer is a function to create an object
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point = Point(10, 20)
point.x = 11
print(point.x)

# exercised
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi I am {self.name}")

john = Person("John Smith")
john.talk()

bob = Person("Bob Baumeister")
bob.talk()

# exercised 2
class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal): # inherit line 29 (dry code/don't repeat code to often)
    def bark(self):
        print("bark")


class Cat(Mammal):
    def meows(self):
        print("meow")

dog1 = Dog()
dog1.bark()
cat1 = Cat()
cat1.meows()