class Car:
    def __init__(self,brand): self.brand=brand
    def start(self): print(self.brand,"starting")

c=Car("Tata"); c.start()

class Math:
    def add(self,a,b): return a+b
m=Math(); print(m.add(2,3))

class Person:
    def __init__(self,name,age): self.name=name; self.age=age
p1=Person("A",20); p2=Person("B",22)
print(p1.name,p2.name)

class Demo:
    def __init__(self,x=10): self.x=x
    def show(self): print(self.x)
Demo().show()
