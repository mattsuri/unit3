#Matthew Suriawinata
#2/26/18
#divisors.py = print divisor of a number

num = int(input("Enter a number ot divide: "))
multi = num

while True:
    if multi == 1:
        break
        
    elif num % multi == 0:
        print(num/multi)
        multi -+ 1
    
