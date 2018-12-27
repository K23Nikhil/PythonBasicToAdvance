#Ask the user for a string and print out whether this string is a palindrome or not. 
#(A palindrome is a string that reads the same forwards and backwards.)

InputString = input("Please Enter a String to check either string is palindrom or not")
lenth = len(myString)
for i in range(0, lenth):
    if(InputString[0] == InputString[lenth-1]):
        print("string is palindrom")
        break
    else:
       print("String is not palindrom")
       break




                 
