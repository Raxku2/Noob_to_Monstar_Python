from random import randint
import pyperclip
import subprocess

listOfCharacter = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM" # 62 / string
listOSpecialCharacter = "!#$%^&*@"

passWord_length = int(input("Enter Password length: "))
specialCharacterInpt = input("Do you want special character? y/n: ")

if specialCharacterInpt.lower() == 'y':
    listOfCharacter = listOfCharacter + listOSpecialCharacter
elif specialCharacterInpt.lower() == 'n':
    pass
else:
    print("Invalid Input!!")

finalPassword = ''

for count in range(passWord_length+1):
    randomIndecForChooseCharacter = randint(0,len(listOfCharacter)-1)
    finalPassword = finalPassword + listOfCharacter[randomIndecForChooseCharacter]
    
print(finalPassword)
pyperclip.set_clipboard("xclip")
pyperclip.copy('Generated Password: ',finalPassword)
print('Copyed to clipboard...')


title = "Password Generator"
message = "Password Copyed in clipboard...'"

subprocess.run(['notify-send', title, message])