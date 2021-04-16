class Student:
    def __init__(self,name,rollno,course,marks):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.marks=marks
    def print(self):
        print(self.name)
        print(self.rollno)
        print(self.course)
        print(self.marks)
lst=[]
f=open("/home/harikrishnan/PycharmProjects/advancedpython/testadvancepython/qno6file","r")
for lines in f:
    data=lines.split(",")
    name=data[0]
    rollno=data[1]
    course=data[2]
    marks=data[3]
    lst.append(marks)
    obj=Student(name,rollno,course,marks)
    obj.print()
f=open("/home/harikrishnan/PycharmProjects/advancedpython/testadvancepython/qno6file","r")
for lines in f:
    data1=lines.split(",")
    if(data1[3]==max(lst)):
        print(lines)
    else:
        pass