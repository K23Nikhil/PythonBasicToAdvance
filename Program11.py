#Ask the user for a number and determine whether the number is prime or not. a prime number is a number that has no divisors.

UserInput = input("Please enter a number to check number is prime or not: ")
UserInput = int(UserInput)

Divisor = []
for i in range(2, UserInput):
    if UserInput % i == 0:
        Divisor.append(i)
if(len(Divisor) > 0):
    print("Your Number is not prime")
    print("Number divisor are: ", Divisor)
else:
    print("Your Number is  prime")