#GLOBAL AND LOCAL VARIABLES(SCOPE OF VARIABLES):
#first case of global variable:
'''a = 3
def check1():
    print("inside value is",a)
check1()
print("outside value is",a)'''


#second case of global variable:
'''a = 4
def check2():
    a = 5
    a = a**2
    print("inside value is",a)
check2()'''


#third case of both global:
'''a = 2
b = 9
def check3():
    a = 7
    print("inside value is",a)
    a = 10
    print("updated value is",b)
    b = 14 #local variable
    b = b+a
    print("value of b is",b)
check3()
print("a value is",a)
print("b value is",b)''' #ERROR


#usage of global keyword:
'''a = 5
def final():
    global a,b
    print("inside value is",a)
    a = 10
    print("updated value is",a)
    #global b
    b = 15
    b = b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)'''


#Student Attendance Tracking Report:
'''def Roll():
    n = int(input("Enter No. of Students: "))
    P_count = int(0)
    A_count = int(0)
    for i in range(1,n+1):
        att = input("Roll No.{} Present(P) or Absent(A): "
        .format(i)).lower()
        if att=="p":
            P_count+=1
        if att=="a":
            A_count+=1
        if att!="a" and att!="p":
            print("Invalid Input!!!")
    print("Attendance Report:\nTotal Students: {}\n
    No. of Students Present: {}\nNo. of Students Absent: {}"
    .format(n,P_count,A_count))
Roll()''' 



