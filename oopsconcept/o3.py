class Employee:
    def setval(self,name,id,age,salary):
        self.id=id
        self.name=name
        self.age=age
        self.salary=salary
    def printval(self):
        print("name:",self.name)
        print("ID:",self.id)
        print("age:",self.age)
        print("salary:",self.salary)
obj=Employee()
obj.setval("HARI",1001,23,25000)
obj.printval()
