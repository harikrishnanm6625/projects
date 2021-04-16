class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print(self.name)
        print(self.age)
class Student(Person):
    def __init__(self,rollno,marks,name,age):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
    def print(self):
        print(self.rollno)
        print(self.marks)
cr=Student(32,23,"Hari",24)
cr.printval()
cr.print()

