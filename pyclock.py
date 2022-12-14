import time
import os

seconds = 0
minutes = 0
hours = 0
days = 0
weeks = 0

while True:
    time.sleep(1)  
    seconds +=1
    os.system("cls")
    print("weeks: " + str(weeks) + " days: " + str(days) + " hours: " + str(hours) + " minutes: "  + str(minutes) + " seconds: " + str(seconds))
    if seconds == 60:
        minutes += 1
        seconds -= 60
    elif minutes == 60:
        minutes -= 60
        hours += 1
    elif hours == 24:
        days += 1
        hours -= 24
    elif days == 7:
        days -= 7
        weeks += 1
