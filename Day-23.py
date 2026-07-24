#MAP()->each object from a collection and forms a new collecion
'''a = [2,3,4,5,6,7,8,9,10,12]
b = [3,4,5,6,7,8,9,10,4,56]
c = list(map(max,a,b))
print(c)
d = list(map(min,a,b))
print(d)'''


#RUN_TIME INPUT FORMATS
#For Strings:
'''a = input("data1")
b = input("data2")
print(a+b)''' #Basic input

'''a,b = input("enter the data").split(",")
print(a+b)''' #Using split

'''a,b = [x for x in input("data").split(",")]
print(a+b)''' #Using list comprehensions

'''a,b = (x for x in input("data").split(","))
print(a+b)''' #Using Generators

'''a,b = map(str,input("Data: ").split(","))
print(a+b)''' #Using Map function

#For Integers:
'''a = int(input("Data1: "))
b = int(input("Data2: "))
print(a+b)''' #Basic input

'''a,b = int(input("Data: ")).split(",")
print(a+b)''' #Error

'''a,b = [int(x) for x in input("Data: ").split(",")]
print(a+b)''' #Using list comprehension

'''a,b = (int(x) for x in input("Data: ").split(","))
print(a+b)''' #Using Generators

'''a,b = map(int,input("Data: ").split(","))
print(a+b)''' #Using Map function

#list:
'''a = list(map(int,input("Data: ").split(",")))
print(a,type(a))'''

#tuple:
'''a = tuple(map(int,input("Data: ").split(",")))
print(a,type(a))'''

#set:
'''a = set(map(int,input("Data: ").split(",")))
print(a,type(a))'''

#Dictionary
'''a = dict(map(int,input("Data: ").split(",")))
print(a,type(a))''' #Error->Map function will not work for dicionaries.

'''a = input("Data: ")
b = dict(i.split(":") for i in a.split(","))
print(b)'''


#Task-1: --->BMI(Body mass index) calculator
weight,height = map(float,input("Enter your Weight(inKg) and Height(inMeters): ").split(","))
BMI = float(weight/(height)**2)
print("Your Calculated BMI: {}".format(BMI))
if BMI<18.5:
    print("You are facing UnderWeight problem.")
if BMI>=18.5 and BMI<=24.9:
    print("Your are Healthy!!!")
if BMI>=25.0 and BMI<=29.9:
    print("You are OverWeight.")
if BMI>=30.0:
    print("Your are Obess.")
    




