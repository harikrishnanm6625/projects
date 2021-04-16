class employee:
    company_name="luminar technolab"
    def __init__(self,name,age,designation):
        self.name=name
        self.age=age
        self.designation=designation
    def printval(self,name,age,designation):
        print(self.name)
        print(self.age)
        print(employee.company_name)
        print(self.designation)
obj=employee('Hari',23,'software developer')
obj.printval('Hari',23,'software developer')