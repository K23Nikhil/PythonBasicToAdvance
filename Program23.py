Array = [1,3,1,8,9,6,4,10,9]
FindPeak = []
for i in range(1, 8):
    if Array[i] > Array[i-1]:
        if  Array[i] > Array[i+1]:
            #print("Number is peak",Array[i])
            FindPeak.append(Array[i])
            
print("Total peak in the input List is ", FindPeak)
    

