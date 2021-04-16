def div_decor(func):
    def inner(no1,no2):
        if no2>no1:
            (no1,no2)=(no2,no1)
        return func(no1,no2)
    return inner
@div_decor
def div(num1,num2):
    return num1/num2
res=div(10,2)
print(res)