try:
    a=int(input("Enter num: "))
    b=int(input("Enter denom: "))
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
finally:
    print("Execution finished")
