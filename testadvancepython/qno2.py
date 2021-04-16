class Person:
    def main1(self,name):
        self.name=name
    def printval(self):
        print(self.name)
class Details(Person):
    def main2(self,age,place):
        self.age=age
        self.place=place
    def print(self):
        print(self.age)
        print(self.place)
class Otherinfo(Details,Person):
    def main3(self,job,salary):
        self.job=job
        self.salary=salary
    def printinfo(self):
        print(self.job)
        print(self.salary)
obj=Otherinfo()
obj.main1("hari")
obj.printval()
obj.main2(23,"kochi")
obj.print()
obj.main3("engineer",25000)
obj.printinfo()




