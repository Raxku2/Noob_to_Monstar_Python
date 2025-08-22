from random import randint
randomNumber = randint(1,100)
count = 0
# print(randomNumber)
while True:
    usrInput = input("Guess the number: ")
    count += 1

    if usrInput.isnumeric():
        # code for game
        if int(usrInput) == randomNumber:
            print("You win!!")
            print(f"You guessed in {count} times!!")
            break
        elif int(usrInput) != randomNumber:
            # print("You guessed it wrong. Try again")

            if int(usrInput) > randomNumber:
                print("You guessed a larger number. Try again")
            else:
                print("You guessed a smaller number. Try again") 
        else:
            print("....")
        pass
    elif usrInput == 'Q':
        print("Quiting...")
        exit()
    else:
        print("Invalid input! Try again...")
