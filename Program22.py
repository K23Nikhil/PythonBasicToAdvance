from itertools import groupby
NamesList = []
with  open('nameslist.txt', 'r') as data:
    for i in data.read().split():
        NamesList.append(i)
        print(i)
sortedList = sorted(NamesList)
num =0
range1 = (len(sortedList) -1)
counts = [(i, len(list(c))) for i, c in groupby(sortedList)]  
for i, c in groupby(sortedList):
    a = len(list(c))
    print(a)
    #print(counts)