#Matthew Suriawianta
#3/1/18
#fri13.py - prints out the next 10 Friday the 13th


from datetime import date

yearNow = date.today().year
monthNow = date.today().month
dayNow = date.today().day

monthAdd = 0
yearAdd = 0


if (dayNow > 13 and yearNow == 12):

if dayNow > 13:
    monthAdd = 1
else:
    monthAdd = 0
    
    
while True:
    if weekday(yearNow + yearAdd, monthNow +monthAdd, 13) == 4:
        print(
    


