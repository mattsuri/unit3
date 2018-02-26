#Matthew Suriawinata
#2/26/18
#divisors.py - print divisor of a number

num = int(input("Enter a number to divide: "))
multi = num

while multi != 1:
    if num % multi == 0:
        print(num/multi)
    multi -= 1
    
