#Write a program (function!) that takes a list and returns a new 
#list that contains all the elements of the first list minus all the duplicates.

fullList = [4,6,2,2,3,76,34,5,7,9,10,11,19,4,65,76,34,3]
newList =[]
#inalList = set(filter(lambda a:a ,fullList))
#print(finalList)
#fullList = sorted(fullList)
#print(fullList)

#for i in fullList:
#    if i not in newList:
#        newList.append(i)
#print(newList)

import pandas as pd

fullList = pd.Series(fullList).drop_duplicates().tolist()
print(fullList)

