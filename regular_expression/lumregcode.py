import re
f2=open("validreg",'w')
rule="([L][U][M][0-9]{2}[P][Y][0-9]{3}$)"
f=open("/home/harikrishnan/PycharmProjects/advancedpython/regular_expression/lumregno","r")
for num in f:
    number=num.rstrip("\n")
    matcher=re.fullmatch(rule,number)
    if matcher!=None:
       f2.write(number)
       f2.write("\n")


