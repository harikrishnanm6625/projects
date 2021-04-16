#single inheritance
class Parent:
    parentname='arun'
    def m1(self,age):
        self.age=age
        print("My name is",Parent.parentname)
        print(self.age)
class Child(Parent):
    def m2(self):
        print("parent name is",Parent.parentname)
        print(self.age)
obj=Child()
obj.m1(23)
obj.m2()