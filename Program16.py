#Write a password generator in Python. Be creative with how you generate passwords 
#- strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random,
# generating a new password every time the user asks for a new password. Include your run-time code in a main methods

import random as rd
import string 
listPassword = []
stringLower = 'abcdefghijklmnopqrstuvwxyz'
stringUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Number = '0123456789'
SpecialChar = '!@#$%^&*()'

length = input("Enter the number for length of the password:" )
length = int(length)
print("Please choose a choice for password:")
choicePassword = input("1 Week Password  2 Medium Password  3 Strong Password  4 SuperStrong Password: ")
choicePassword = int(choicePassword)
if choicePassword == 1:
    weekPassword = "".join(rd.choice(stringLower)  for x in range(length)) 
    print(weekPassword)
elif choicePassword == 2:
    MediumPassword = "".join(rd.choice(Number)+ rd.choice(stringLower) for x in range(length))
    print(MediumPassword)
elif choicePassword == 3:
    StrongPassword = "".join(rd.choice(Number)+ rd.choice(stringLower) for x in range(length))
    print(StrongPassword)
elif choicePassword == 4:
    SuperStrongPassword = "".join(rd.choice(Number)+ rd.choice(stringLower) +rd.choice(SpecialChar)+ rd.choice(stringUpper) for x in range(length))
    print(SuperStrongPassword)
else:
    print("choose a correct input")



