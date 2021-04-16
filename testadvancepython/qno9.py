import re
r=input("enter code")
x="[A-Z]{1}[a-z]{1}"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start ())
    print(match.group ())