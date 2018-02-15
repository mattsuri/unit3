#Matthew Suriawinata
#2/15/18
#coutdown.py - counts down

num = int(input("Enter a number of seconds: "))



while True:
    num -= 1
    if num == 0:
        print("BOOM")
        break
    print(num)
    
    
