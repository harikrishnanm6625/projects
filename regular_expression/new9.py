import re
r=input("enter the value")
x="[A-Za-z]+[0-9]{1}$"
match=re.fullmatch(x,r)
if match is not None:
    print("valid")
else:
    print("invalid")
