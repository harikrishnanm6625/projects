employes={
    1000:{"name":"sajay","desig":"python trainer","exp":3},
    1001: {"name": "sabir", "desig": "bigdata trainer", "exp": 3},
    1002:{"name":"christy","desig":"ml","exp":3}
}

def emp_details(**kwargs):
    id=kwargs["eid"]
    prop=kwargs["prop"]
    if(id in employes):
        print(employes[id]["name"])
        print(employes[id][prop])
    else:
        print("doesnt exist")
emp_details(eid=1000,prop="desig")