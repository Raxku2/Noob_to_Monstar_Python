class Animal:
    def speak(self): print("Sound")

class Dog(Animal):
    def speak(self): print("Bark")

a=Animal(); d=Dog()
a.speak(); d.speak()
