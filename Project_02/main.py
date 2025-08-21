def c_to_f(c): return (c*9/5)+32
def f_to_c(f): return (f-32)*5/9
def c_to_k(c): return c+273.15
def k_to_c(k): return k-273.15
def f_to_k(f): return (f-32)*5/9+273.15
def k_to_f(k): return (k-273.15)*9/5+32

while True:
    print("\n=== Temperature Converter ===")
    print("1.C→F  2.F→C  3.C→K  4.K→C  5.F→K  6.K→F  7.Exit")
    ch=input("Enter choice: ")
    if ch=="7": break
    
    val=float(input("Enter temperature: "))
    
    if ch=="1": print("Result:",c_to_f(val),"F")
    elif ch=="2": print("Result:",f_to_c(val),"C")
    elif ch=="3": print("Result:",c_to_k(val),"K")
    elif ch=="4": print("Result:",k_to_c(val),"C")
    elif ch=="5": print("Result:",f_to_k(val),"K")
    elif ch=="6": print("Result:",k_to_f(val),"F")
    else: print("Invalid choice")
