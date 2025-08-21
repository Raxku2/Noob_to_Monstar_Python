def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return "Error: Divide by zero" if b==0 else a/b
def power(a,b): return a**b

while True:
    print("\n=== Calculator CLI ===")
    print("1.Add  2.Subtract  3.Multiply  4.Divide  5.Power  6.Exit")
    choice=input("Enter choice: ")
    if choice=="6": break
    
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))

    if choice=="1": print("Result =",add(a,b))
    elif choice=="2": print("Result =",sub(a,b))
    elif choice=="3": print("Result =",mul(a,b))
    elif choice=="4": print("Result =",div(a,b))
    elif choice=="5": print("Result =",power(a,b))
    else: print("Invalid choice")
