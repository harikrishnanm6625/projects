import re
f2=open("regstrn","w")
f=open("/home/harikrishnan/PycharmProjects/advancedpython/regular_expression/lumregno","r")
x="[L][U][M]\d{2}[P][Y]\d{3}"
for lines in f:
    num=lines.rstrip("\n")
    match=re.fullmatch(x,num)
    if match!=None:
        f2.write(num)
        f2.write("\n")
    else:
        pass


