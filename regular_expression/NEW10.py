import re
r=input("enter the value")
x="^a[a-zA-Z0-9\W]*b$"
match=re.fullmatch(x,r)
if match is not None:
    print("valid")
else:
    print("invalid")