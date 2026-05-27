class Dog:
    def __init__(self, name, age, house):
        self.name = name
        self.age = age
        self.house = house

    def bark(self):
        print (self.name + " says woof!")

d1 = Dog("Violeta", 4, "Casa 2")

d1.bark()
