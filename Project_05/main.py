from random import randint

randomNumber = randint(0,2)
option = ['Rock','Paper','Scissor']

systemChoice = option[randomNumber]

while True:
    usrInput = input("Enter ('1' for Rock), ('2' for Paper), ('3' for Scissor), ('Q' for quit): ") #string

    if usrInput.isnumeric() and (usrInput in ['1','2','3']):
        # code for game
        userChoiceIndex = int(usrInput) -1
        usrChoice = option[userChoiceIndex]

        print(f"you choose {usrChoice}")
        print(f"computer choose {systemChoice}")

        if ((userChoiceIndex == 0 and randomNumber == 1) or 
            (userChoiceIndex == 1 and randomNumber == 2) or 
            (userChoiceIndex == 2 and randomNumber == 0) ):
            # computer win
            print("computer win")
            
        elif ((randomNumber == 0 and userChoiceIndex == 1) or 
              (randomNumber == 1 and userChoiceIndex == 2) or 
              (randomNumber == 2 and userChoiceIndex == 0))  :
            # user win
            print("you win")
            
        else:
            print("game draw...")
            


        break
    elif usrInput == 'Q':
        print("Quiting...")
        exit()
    else:
        print("Invalid input! Try again...")
