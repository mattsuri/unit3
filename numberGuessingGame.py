#Matthew Suriawianta 
#2/26/18
#guessingGame.py - guess a number game

from random import randint 


number = randint(1,100)
atempts = 1 

while True:
    guess = int(input("Enter a guess between 1 and 100"))
    if guess > number:
        atempts += 1
        print("Too high")
    if guess < number:
        atempts += 1
        print("Too low")
    else:
        print("Your guess is right!")
        print("It took you", atempts, " tries")
        break
    
    
