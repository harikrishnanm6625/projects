class Student:
    def __init__(self,name,rolno,course,marks):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.marks=marks
    def printval(self):
        print("name=",self.name)
        print("rollno=",self.rollno)
        print("course=",self.course)
        print("marks=",self.marks)
    def __str__(self):
        return self.course
        return self.name
f=open("/home/harikrishnan/PycharmProjects/advancedpython/oopsconcept/ stud ent",'r')
for line in f:
    data=line.split(",")
    if(int(data[3])>190):
        name=data[0]
        rollno=data[1]
        course=data[2]
        marks=data[3]
        obj=Student(name,rollno,course,marks)
        obj.printval()
    else:
        pass

