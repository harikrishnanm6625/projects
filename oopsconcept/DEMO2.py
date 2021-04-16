class Person:
    def setval(self,name,age):
        self.age=age
        self.name=name
    def printval(self):
        print("name:",self.name)
        print("age:",self.age)
obj=Person()
obj.setval("HARI",23)
obj.printval()
