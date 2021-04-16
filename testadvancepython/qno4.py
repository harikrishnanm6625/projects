class Animal:
    def __init__(self,animalname,age):
        self.animalname=animalname
        self.age=age
    def print(self):
        print(self.animalname)
        print(self.age)
class Dog(Animal):
    def __init__(self,animalname,age,food):
        super().__init__(animalname,age)
        self.food=food
    def printval(self):
        print(self.food)
obj=Dog("dog",7,"meat")
obj.print()
obj.printval()
