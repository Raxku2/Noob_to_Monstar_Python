n=int(input())
print("Positive" if n>0 else "Negative")

for i in range(1,11): print(i)

for i in range(2,21,2): print(i)

print(sum(range(1,11)))

n=int(input())
fact=1
for i in range(1,n+1): fact*=i
print(fact)

n=int(input())
for i in range(1,11): print(n,"x",i,"=",n*i)

s="hello"; rev=""
for ch in s: rev=ch+rev
print(rev)

for i in range(10):
    if i==5: break
    print(i)

for i in range(10):
    if i%2==0: continue
    print(i)

for i in range(3):
    for j in range(3):
        print(i,j,end=" ")
    print()
