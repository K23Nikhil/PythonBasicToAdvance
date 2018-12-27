
def GetNumber():
    inputNo = input("Please Enter a number which you want to search on List: ")
    inputNo = int(inputNo)
    return inputNo

def SearchNoInList():
    NumbersList = [1,4,5,34,23,51,90,45,87,66,54,38,97,18,76]
    print("Availbel List:",NumbersList)
    SearchNo = GetNumber()   
    NumbersListRange = (len(NumbersList)-1)
    NumbersListRange = int(NumbersListRange)
    
    for i in range(0, 13, +1):
        if(NumbersList[i] == SearchNo):
            print("Number is available in List", SearchNo)
            break
        else:
            print("Number is not available")
            break
def main():
    SearchNoInList()

__name__ = "__main__"
main()