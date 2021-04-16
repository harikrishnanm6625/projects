import re
n=input("enter email")
x="[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[A-Za-z0-9]+$"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")