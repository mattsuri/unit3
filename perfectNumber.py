#Matthew Suriawianta
#3/1/18
#perfectNumber.py - Find if number is perfect

total = 0
num = int(input("Enter a number: ")
divisor = num - 1

while divisor>0:
    if num % divisor == 0:
        total += divisor
    divisor -=1
    
if total == num:
    print("Perfect Number!")
else:
    print("Not Perfect Number.")
