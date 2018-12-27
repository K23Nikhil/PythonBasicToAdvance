Numbers = [2,4,5,1,6,7,8,9,43,46,76,23,66,80]
evenNumber = list(filter(lambda a:a % 2, Numbers))
oddNumber = list((lambda b: b % 2, Numbers))
#print(oddNumber)
print(evenNumber)
