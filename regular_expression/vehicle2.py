import re
f2=open("validreg",'a')
rule="[kK][lL]\d{2}[a-zA-Z]{2}\D{4}$"
f=open("/home/harikrishnan/PycharmProjects/advancedpython/regular_expression/vehnum","r")
for num in f:
    number=num.rstrip("\n")
    matcher=re.fullmatch(rule,number)
    if matcher!=None:
        f2.write(number)
        f2.write("\n")

