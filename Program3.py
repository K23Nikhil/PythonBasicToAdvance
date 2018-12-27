listVariable = [1,2,87, 65, 87,00, 65, 56, 74,34,56,69,91, 23, 34, 55]
tempList = []
GreatorList = input("Please Enter a No which you want to featch all record greator then that no: ")
GreatorNo = int(GreatorList)
for i in listVariable:
    if i > GreatorNo:
        tempList.append(i)
#print("All Records Greator then %s "% GreatorNo, "   ", tempList)

#Another way to filter records from list
#print(list(filter(lambda x: x < 50, listVariable)))
print(list(filter(lambda x: x < 50, listVariable)))
