num1=int(input("enter the number"))
num2=int(input("enter second no2"))
try:
    c=num1/num2
    print(c)
except:
    print("exception occured")
finally:
    print("inside finally")