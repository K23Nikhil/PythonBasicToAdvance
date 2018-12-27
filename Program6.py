#Match the comon element in both list and add into another list 
mylist1 = [1, 10,13, 15,32,23,54,76,8,96]
mylist2 = [1, 10,19, 15,2,23,54,6,8,96,88,48]

tempList = []
for i in range(0, len(mylist1)):
    for j in range(0, len(mylist2)):
        if mylist1[i] == mylist2[j]:
            tempList.append(mylist2[j])
print(tempList)
