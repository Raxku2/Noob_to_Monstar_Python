def add(a,b): return a+b

def even_odd(n): return "Even" if n%2==0 else "Odd"

def fact(n):
    f=1
    for i in range(1,n+1): f*=i
    return f

def greet(name="User"): return "Hello "+name

def calc(a,b): return a+b,a-b

def square(x): return x*x

def isprime(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True

def reverse(s): return s[::-1]

x=5
def local_demo():
    x=10
    print("Local",x)
local_demo(); print("Global",x)

def sum_n(n): return 1 if n==1 else n+sum_n(n-1)
