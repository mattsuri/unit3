#Matthew Suriawinata 
#2/28/18
#warmup8.py - Find the sum of all numbers less than 100,000 that are divisible by 3, 10, and 17


total = 0
num = 100000

while num>0:
    if num % 3 == 0 and num % 10 == 0 and num % 17 == 0:
        print(num)
    num -=1
    
        
