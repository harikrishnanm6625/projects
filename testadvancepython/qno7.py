import re
f2=open("mobleno","w")
f=open("/home/harikrishnan/PycharmProjects/advancedpython/testadvancepython/qno7file","r")
x="[+][9][1]\d{10}$"
for lines in f:
    num=lines.rstrip("\n")
    match=re.fullmatch(x,num)
    if match is not None:
        f2.write(num)
        f2.write("\n")
