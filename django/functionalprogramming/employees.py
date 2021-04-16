class Employee:
    def __init__(self,eid,ename,design,salary):
        self.eid=eid
        self.ename=ename
        self.design=design
        self.salary=salary
    def __str__(self):
        return self.ename
obj1=Employee(1001,"arun","analyst",28000)
obj2=Employee(1002,"HARI","developer",25000)
obj3=Employee(1003,"ram","developer",240000)

employeelst=[]
employeelst.append(obj1)
employeelst.append(obj2)
employeelst.append(obj3)
#print(employeelst) #we have to use for loop
#print(employeelst[0])#---because two string method is used
designe=list(map(lambda n:n.design,employeelst))
print(designe)
namesofe=list(map(lambda num:num.ename,employeelst))
print(namesofe)
salarytotal=list(map(lambda emp:emp.salary,employeelst))
print(salarytotal)
print(max(salarytotal))
developers=list(filter(lambda emp:emp.design=="developer",employeelst))
for lines in developers:
     print(lines)