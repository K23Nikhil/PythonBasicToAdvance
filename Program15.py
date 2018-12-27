#Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
#My name is Michele Then I would see the string: #Michele is name My


StringList = []
inputString = input("Please enter a string: ")
for word in inputString.split(" "):
    StringList.append(word)
stringLen = len(StringList) -1
print("String Lenth is:", stringLen)
for i in range(stringLen, 0, -1):
     print(StringList[i])