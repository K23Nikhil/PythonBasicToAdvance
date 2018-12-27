"-------------------------Lecture 1----------------------------------------------"
print ("Hello")

#Assign value in single line
a,b,c = 10, 20, 30 

""" Multiline Statement can be use using the  \ opreator  """
d = a + \
    b + \
    c
print("Here is Sum of Give Input :", d)

#touple Example
a = ("Ram", "Shyam","Arun","Kapil")

# DataType Conversion
OrderNo = 124532
charactor = "A"
#Long is no longer supported in Python 3.x version use int instead of Long
OrderNoConvert = int(OrderNo)
print(OrderNoConvert)
print(ord(charactor))
"""Convert the string in touple using the tuple function"""
print(tuple(charactor))

#Conditionl Practises
age1 = input("Please enter Age to check Kid Teen or Adult")
age = int(age1)
if age < 15:
    print("Your child is Kid")
elif age > 15 and age < 18:
    print("Your child is young")
elif age > 18 and age < 35:
    print("Your child is teen")
else:
    print("Your child is old and his age is :", age)


# Loop Practise
count = 0 
while (count < 10):   
    print(count)
    count = count + 1
    
print("Loop Executed")






















