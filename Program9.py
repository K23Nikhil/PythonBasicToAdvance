#Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right

import random

UserRecord = []
def game():
        inputNoFromUser = input("Please give a input No and check if the number is low or high: ")
        inputNo = int(inputNoFromUser)
        GenratedRandomNo = int(random.randint(0,9))
        if inputNo == GenratedRandomNo:
            print("You have choose exactly same No, Random No is: ", GenratedRandomNo)
            UserRecord.append(inputNo)
        elif inputNo < GenratedRandomNo:
            print("You choose low no, Random No is: ", GenratedRandomNo)
            UserRecord.append(inputNo)
        elif inputNo > GenratedRandomNo:
            print("Your No is greator, Random No is: ", GenratedRandomNo)
            UserRecord.append(inputNo)
        return UserRecord

def checkUserInput():
     inputUser = input("if you want to exit from game press 1 or continue 0 :" )
     inputUser = int(inputUser)
     if (inputUser ==1):
         print("You want to terminate game")
     elif(inputUser == 0):
         print("You want to play again")
     else:
         print("Choose a correct input")      
     return inputUser

def main():
    game()
    while True:
        UserInput = checkUserInput()
        if(UserInput == 1):          
          HitTrial = len(UserRecord)
          print("Thanks for participating in choose a correct No game:")
          print("Your Total Trial:", HitTrial)
          break
        elif UserInput == 0: 
             game()
        else:
            checkUserInput()
            

__name__ = "__main__"
main()




