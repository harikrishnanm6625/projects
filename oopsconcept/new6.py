#multi level inheritance
class Parent:
    parentname='arun'
    def m1(self,age):
        self.age=age
        print("My name is",Parent.parentname)
        print(self.age)
class Mobile(Parent):
    def m3(self,cname):
        self.cname=cname
        print(self.cname)
        print("my mobile is 1+")
class Child(Mobile):
    def m2(self,sdc):
        self.sdc=sdc
        print(self.sdc)
        print("parent name is",Parent.parentname)
obj=Child()
obj.m2(23)
obj.m3(245)
obj.m1("sdc")

