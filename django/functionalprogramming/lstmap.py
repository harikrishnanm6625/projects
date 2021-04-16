lst=[4,2,1,6,7,8]
#output--3,1,0,7,8,9
lst1=[]
for num in lst:
    if(num<5):
        num1=num-1
        lst1.append(num1)
    elif(num>5):
        num2=num+1
        lst1.append(num2)
    else:
        pass
print(lst1)
num1=list(map(lambda no:no-1 if no<=5 else no+1,lst))
print(num1)
result=list(map(lambda num:num-1 if num<5 else num+1,lst))
print(result)