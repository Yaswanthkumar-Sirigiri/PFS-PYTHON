#CONDITIONS
#IF-CONDITION BY USING "COMPARISION OPERATORS"
#<,>,<=,>=,!=,==
'''a = 4
b = 10
if a<b:
    print("a is less than b")'''


'''a = 4
b = 2
if a>b:
    print("a is greater than b")'''


'''a = 4
b = 5
if a <= b:
    print("a is less than or equal to b")'''


'''a = 6
b = 5
if a >= b:
    print("a is greater than or equal to b")'''


'''a = 4
b = 5
if a != b:
    print("a is not equal to b")'''


'''a = 5
b = 5
if a==b:
    print("a is equal to b")'''


'''a = int(input("enter the value: "))
b = int(input("enter the value: "))
if a <= b:
    print("a is less than or equal to b")'''


'''a = int(input("enter the value"))
if a < 10:
    print("a is less than 10")'''


'''a = "python"
if a=="java":
    print("True")'''


'''a = input("data")
if a == "java":
    print("True")'''   


#IF-CONDITION BY USING LOGICAL OPERATORS
#AND, OR, NOT
'''a = 4
b = 9
if a<b and a>b:
    print("less")'''



'''a = 4
b = 9
if a<=b and b>=a:
    print("less")'''


'''a = 4
b = 9
if a!=b and a==b:
    print("True")'''


'''a = 4
b = 9
if a==b or a<b:
    print("True")'''



'''a = 4
b = 9
if not a>b or a<10:
    print("True")'''


'''a = int(input("enter value: "))
b = int(input("Enter the value: "))
if a>b and a>100:
    print("a is GReateRRRR")'''


#IF-CONDITION BY USING IDENTIFY OPERATORS
#IS, IS NOT
'''a = 1
if type(a) is int:
    print("A is Integer")'''


'''a = "hello"
if type(a) is not int:
    print("A is not integer")'''


'''a = 12.2
if type(a) is float:
    print("A is Float")'''


'''a = 23
if type(a) is not float:
    print("A is not float")'''


'''a = "hello"
if type(a) is str:
    print("A is string")'''


'''a = 123
if type(a) is not str:
    print("A is not string")'''


#IF-CONDITION USING MEMBERSHIP OPERATORS
'''a = 2,3,4,5,6,7,8,9,10
if 10 in a:
    print("true")'''


'''a = 2,3,4,5,6,7,8,9,10
if 20 in a:
    print("true")'''


'''a = 2,3,4,5,6,7,8,9,10
if 20 not in a:
    print("False")'''


'''a = int(input("Enter the value: "))
if 30 in a:
    print("True")'''#ERROR


'''a = 2,3,4,5,6,7,8,9,10
b = int(input("enter a value: "))
if b in a:
    print("True")'''
