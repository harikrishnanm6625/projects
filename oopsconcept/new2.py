class Employee:
    cname="luminar_technolab"
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
    def printval(self):
        print(self.name)
        print(Employee.cname)
        print(self.age)
        print(self.id)
obj=Employee("HARI",23,1001)
obj.printval()
