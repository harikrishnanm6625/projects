import re
r=input("enter the code")
x="[a-zA-Z0-9\W]{8,15}"
match=re.fullmatch(x,r)
if match is not None:
    print("valid")
else:
    print("invalid")