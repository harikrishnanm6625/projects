class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mult(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
obj=Calc(2,3)
print(obj.add())
print(obj.sub())
print(obj.mult())
print(obj.div())