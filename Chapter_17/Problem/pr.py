class Animal:
    def speak(self): print("Generic")

class Dog(Animal):
    def speak(self): print("Bark")

def poly(obj): obj.speak()
poly(Animal()); poly(Dog())

class Bank:
    def __init__(self): self.__balance=0
    def deposit(self,a): self.__balance+=a
    def get(self): return self.__balance

b=Bank(); b.deposit(100); print(b.get())

class Vehicle: pass
class Car(Vehicle): pass
class ElectricCar(Car): pass

class A: pass
class B: pass
class C(A,B): pass

class Parent:
    def __init__(self): print("Parent")
class Child(Parent):
    def __init__(self):
        super().__init__(); print("Child")
Child()

print(isinstance(Dog(),Animal))
