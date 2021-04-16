from functools import reduce #map and filter are builtin but reduce we have to import from functools

lst=[10,20,30,50,80]
sum=reduce(lambda no1,no2:no1+no2,lst)
print(sum)
total=reduce(lambda no1,no2:no1+no2,lst)
print(total)


max=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst )
print(max)

min=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
print(min)