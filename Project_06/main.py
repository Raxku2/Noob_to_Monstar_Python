def length_converter():
    print("\nLength Conversion Options:")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")
    print("3. Centimeters to Inches")
    print("4. Inches to Centimeters")
    choice = int(input("Enter choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print(f"{value} m = {value / 1000} km")
    elif choice == 2:
        print(f"{value} km = {value * 1000} m")
    elif choice == 3:
        print(f"{value} cm = {value / 2.54} in")
    elif choice == 4:
        print(f"{value} in = {value * 2.54} cm")


def weight_converter():
    print("\nWeight Conversion Options:")
    print("1. Kilograms to Grams")
    print("2. Grams to Kilograms")
    print("3. Pounds to Kilograms")
    print("4. Kilograms to Pounds")
    choice = int(input("Enter choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print(f"{value} kg = {value * 1000} g")
    elif choice == 2:
        print(f"{value} g = {value / 1000} kg")
    elif choice == 3:
        print(f"{value} lbs = {value * 0.4536} kg")
    elif choice == 4:
        print(f"{value} kg = {value / 0.4536} lbs")


def temp_converter():
    print("\nTemperature Conversion Options:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    choice = int(input("Enter choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print(f"{value}°C = {(value * 9/5) + 32}°F")
    elif choice == 2:
        print(f"{value}°F = {(value - 32) * 5/9}°C")
    elif choice == 3:
        print(f"{value}°C = {value + 273.15} K")
    elif choice == 4:
        print(f"{value} K = {value - 273.15}°C")


def main():
    while True:
        print("\n=== Unit Converter ===")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")

        option = int(input("Choose option: "))
        if option == 1:
            length_converter()
        elif option == 2:
            weight_converter()
        elif option == 3:
            temp_converter()
        elif option == 4:
            print("Exiting...")
            break
        else:
            print("Invalid option!")



main()
