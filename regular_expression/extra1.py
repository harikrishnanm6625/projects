import re
x="[a-zA-z]+\d{1}$"
r=input("enter the code")
match=re.fullmatch(x,r)
if match is not None:
    print("valid")
else:
    print("invalid")