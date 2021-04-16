num1=int(input("enter no1"))
num2=int(input("enter no2"))
try:
    r=num1/num2
except:
    print("exception occured")
finally:
    print("division")