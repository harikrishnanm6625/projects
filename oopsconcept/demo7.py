class Employee:
    cname="luminar technolab"
    def setval(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
    def printval(self):
        print(Employee.cname)
        print(self.name)
        print(self.age)
        print(self.id)
obj=Employee()
obj.setval("HARI",23,1001)
obj.printval()