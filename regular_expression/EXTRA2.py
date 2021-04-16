import re
r=input("enter the code")
x="(^a[a-zA-Z\W\d]*b$)"
match=re.fullmatch(x,r)
if match is not None:
    print("valid")
else:
    print("invalid")