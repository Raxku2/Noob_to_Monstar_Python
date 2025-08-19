f=lambda x:x*x
add=lambda a,b:a+b

nums=[1,2,3,4]
print(list(map(lambda x:x*2,nums)))
print(list(filter(lambda x:x%2==0,nums)))

from functools import reduce
print(reduce(lambda x,y:x*y,nums))

rev=lambda s:s[::-1]

words=["hi","bye"]
print(list(map(lambda w:w.upper(),words)))

print(list(filter(lambda x:x>10,[5,12,7,20])))

print(reduce(lambda x,y:x if x>y else y,[2,9,7,5]))

print(list(map(lambda x:x*x,filter(lambda x:x%2==0,nums))))
