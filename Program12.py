#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes 
#a new list of only the first and last elements of the given list. For practice

InputNoList = []
FinalList = []
TotalNo = input("Enter the total number which you want to add in list: ")  
TotalNo = int(TotalNo)
for i in range(0, TotalNo):
    inputNo = input("Enter a elemnet for list")
    inputNo = int(inputNo)
    InputNoList.append(inputNo)
print("Your Given Input List is:", InputNoList)
FinalList.insert(0,InputNoList[0])
FinalList.insert(TotalNo-1, InputNoList[len(InputNoList)-1])
print("First and Last Index Value of the list is:", FinalList)