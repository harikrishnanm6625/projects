employes={
    1000:{"name":"sajay","desig":"python trainer","exp":3},
    1001: {"name": "sabir", "desig": "bigdata trainer", "exp": 3},
    1002:{"name":"christy","desig":"ml","exp":3}
}

eid=int(input("employee id"))

if(eid in employes):
    print(employes[eid]["name"])
else:
    print("doesnt exist")

