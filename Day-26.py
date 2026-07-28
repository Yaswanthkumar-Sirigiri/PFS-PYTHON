#CALENDAR MODULE:
'''import calendar
year =  2006
month = 8
print(calendar.month(year,month))''' #Prints only specified month calendar

'''import calendar
year = 2006
print(calendar.calendar(year))''' #Prints whole specified year calendar

'''import calendar
year = int(input("Enter Year: "))
month = int(input("Enter Month: "))
print(calendar.month(year,month))
print("=========================")
print(calendar.calendar(year))''' #Runtime Input Combined


#DATETIME MODULE:
'''from datetime import date
a = date.today()
print(a)'''

'''import datetime
a = datetime.datetime.now()
print(a)'''

#TIME:
'''import time
a = time.time()
print(a)

b = time.localtime(a)
print(b)

print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")

print(f"Time is {b.tm_hour}-{b.tm_min}-{b.tm_sec}")

print(f"Day is {b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")'''


'''import random,time
for i in range(10):
    a = random.randint(1000,9999)
    print(a)
    time.sleep(2)'''


#ERROR HANDLING:
#Types of Errors:
#-->syntax error:
'''for i in range(10)
print(i)'''

#-->runtime error:
'''a = int(input("a value"))
b = int(input("b value"))
Print(a//b)'''

#-->logical error:
'''a = 10
b = 20
if a<b:
    print("less")'''





