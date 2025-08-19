from functools import reduce

f=lambda x: x*x
print(f(5))

nums=[1,2,3,4]
print(list(map(lambda x:x*2, nums)))
print(list(filter(lambda x:x%2==0, nums)))
print(reduce(lambda x,y:x+y, nums))
