#Find the Devisor of Given Numbers
InputNo = input("Please enter the number to get the devisior: " )
Number = int(InputNo)
i =1
while i <= Number:
    if Number % i == 0:  
        print(i)
    i = i + 1
        
        
