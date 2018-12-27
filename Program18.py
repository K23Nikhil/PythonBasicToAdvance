import random as rd
mylist = []
Number = rd.randrange(1111, 9999)
mylist = [int(i) for i in str(Number)]
print(mylist)

input = input("Please enter the 4 digit Number to check Cow and Bull: ")

inputList = [int(i) for i in str(input)]

Status = []
for i in  range(0,4):
    if mylist[i] == inputList[i]:
        Status.append("COW")
        #print("cow")
    else:
        Status.append("BULL")
        #print("Bull")
#print("Number of Cow is:", Status)
print(Status)
Cowcount = 0
BullCount = 0
range1 = (len(Status)- 1)
rangeNo = int(range1)
print(rangeNo)
for i in range(0,rangeNo):
    if Status[i] == "COW":
        Cowcount = Cowcount +1 
    elif Status[i] == "BULL":
        BullCount = BullCount + 1
        
print("Number of Cow is:", Cowcount)
print("Number of Bull is:", BullCount)


