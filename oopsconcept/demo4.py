class Bank:
    def accreate(self,name,bname,accno):
        self.name=name
        self.bname=bname
        self.accn0=accno
        self.minbalance=5000
        self.balance=self.minbalance
    def deposit(self,amt):
        self.balance+=amt
        print("the credited amount is",amt)
        print("the total balance is",self.balance)
    def withdraw(self,amt):
        if(amt>self.balance):
            print("insufficient balance")
        else:
            self.balance-=amt
            print("available balance",self.balance)
obj=Bank()
obj.accreate("hari","sbi",121)
obj.deposit(1200)
obj.withdraw(2000)