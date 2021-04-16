def print_person_details(**args):
    print(args)
print_person_details(name="ajay",birthplace="trissur",wplace="kakkanad")

def add(*args):
    print(args)
    sum=0
    for i in args:
        sum+=i
    return sum

res=add(10,20,30,40)
print(res)