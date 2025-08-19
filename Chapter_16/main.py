class Student:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print("Hello",self.name)

s=Student("Rahul")
s.greet()
