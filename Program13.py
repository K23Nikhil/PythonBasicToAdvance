#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.

startIndex = 0
endIndex = 10
FabSer = []
i = 1

if startIndex ==1:
    FabSer.append(startIndex)
    FabSer.append(startIndex)
else:
    FabSer.append(startIndex)
    FabSer.append(startIndex + 1)

while i < endIndex:
        sum = FabSer[i] + FabSer[i -1]
        FabSer.append(sum)
        i = i+1
print(FabSer)

    