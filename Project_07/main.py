import random

def roll_dice(n=1):
    results = [random.randint(1, 6) for _ in range(n)]
    return results

def main():
    print("🎲 Welcome to Dice Roller 🎲")
    while True:
        try:
            num = int(input("How many dice to roll? "))
            results = roll_dice(num)
            print("You rolled:", results)
        except ValueError:
            print("Invalid input. Enter a number!")

        again = input("Roll again? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break


main()
