#multiple inheritance
class Parent:
    parentname='arun'
    def m1(self,age):
        self.age=age
        print("My name is",Parent.parentname)
        print(self.age)
class Mobile:
    def m3(self):
        print("my mobile is 1+")
class Child(Parent,Mobile):
    def m2(self):
        print("parent name is",Parent.parentname)
        print(self.age)
obj=Child()
obj.m1(23)
obj.m2()
obj.m3()