#MATH MODULE:
'''import math
print(math.pi)
print(math.pi*3)
print(math.sqrt(2))
print(math.pow(2,2))
print(math.log(10))
print(math.tan(45))
print(math.cos(60))
print(math.sin(30))
print(math.ceil(4.9))
print(math.floor(4.9))'''


#FROM KEYWORD:
'''from math import pi,sqrt,log,tan,cos
print(pi)
print(sqrt(2))
print(log(20))
print(tan(45))
print(cos(60))'''


#SYS MODULE
'''import sys
print(sys.path)   #--->Python location
print(sys.version)#--->Python version'''


#OS MODULE
'''import os
print(os.path)
print(os.getcwd())
print(os.listdir())
print(os.chdir("D:\DESK\TEMP"))
print(os.listdir())
print(os.mkdir("july27"))'''


#RANDOM MODULE:
'''import random
a = random.sample(range(20,40),10)
print(a)'''


#RANDINT():
'''import random
a = random.randint(20,50)
print(a)'''


#CHOICE():
'''import random
a = [10,30,50,60,80]
b = random.choice(a)
print(b)'''


#Task-1:
import random
def Dice():
    inp = int(input("Enter the Roll of Dice: "))
    a = random.randint(1,7)
    print("You got: ",a)
    inpp = input("Enter 0->To Roll again, 1->To Exit: ")
    if inpp=="0":
        Dice()
    if inpp=="1":
        return
Dice()



