#Matthew Suriawianta
#3/1/18
#warmup9.py - Ask user to enter text 


text = input("Enter some text: ")

text = (text.lower())


for ch in text:
    if ch == "a" or ch == "e"or ch == "o" or ch == "i" or ch == "u":
        print(ch.upper())
    else:
        print(ch.lower())
