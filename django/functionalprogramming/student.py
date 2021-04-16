class Student:
    def __init__(self,rollno,name,course,total):
        self.rollno=rollno
        self.name=name
        self.course=course
        self.total=total
    def __str__(self):
        return self.name
obj1=Student(1,"arun","bba",250)
print(obj1)
obj2=Student(2,"hari","mba",200)
obj3=Student(3,"alex","bba",150)
stlst=[]
stlst.append(obj1)
stlst.append(obj2)
stlst.append(obj3)
sttotal=list(map(lambda stud:stud.total,stlst))
print(sttotal)
print(max(sttotal))
