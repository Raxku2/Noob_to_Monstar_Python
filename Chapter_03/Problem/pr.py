name = input("Enter your name: ")
print("Hello", name + "!")

a = int(input("Enter first: "))
b = int(input("Enter second: "))
print("Sum =", a + b)

age = int(input("Enter age: "))
print("You are", age, "years old")

r = float(input("Enter radius: "))
print("Area =", 3.14 * r * r)

x, y, z = map(int, input("Enter 3 numbers: ").split())
print("Average =", (x+y+z)/3)

marks = int(input("Enter marks: "))
print("Pass" if marks>=40 else "Fail")

city = input("Enter city: ")
print("Welcome to", city)

x = int(input())
y = int(input())
print("Add:", x+y, "Multiply:", x*y)

side = int(input("Side: "))
print("Perimeter =", 4*side)

# Answer: input() reads everything as text, so returns str.
